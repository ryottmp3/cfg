# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess

mod = "mod4"
terminal = guess_terminal()
kitty = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn rofi"),

    # screenshot utility
    Key([mod], "p", lazy.spawn("scrot ~/pictures/Sceenshots/%Y-%m-%d-%T-screenshot.png"), desc="Takes a screenshot"),

    # Volume Control
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lowers Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raises Volume by 5%"),

]
groups = [
    # Screen affinity to ensure windows are on the right screen
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0),
    Group(name="4", screen_affinity=0),
    Group(name="5", screen_affinity=1),
    Group(name="6", screen_affinity=1),
    Group(name="7", screen_affinity=1),
    Group(name="8", screen_affinity=1),
    Group(name="9", screen_affinity=2),
    Group(name="0", screen_affinity=2),
]

def go_to_group(name: str):
    def _inner(qtile) -> None:
        # If there's only one screen, have them all on the same screen.
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        elif len(qtile.screens) == 2:
            if name in '12345':
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in '67890':
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()

        elif len(qtile.screens) == 3:
            if name in '1234':
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in '5678':
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()
            elif name in '90':
                qtile.focus_screen(2)
                qtile.groups_map[name].toscreen()

    return _inner


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        elif len(qtile.screens) == 2:
            if name in "12345":
                qtile.current_window.togroup(name, switch_group=False)
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in "67890":
                qtile.current_window.togroup(name, switch_group=False)
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()
        elif len(qtile.screens) == 3:
            if name in "1234":
                qtile.current_window.togroup(name, switch_group=False)
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in "5678":
                qtile.current_window.togroup(name, switch_group=False)
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()
            elif name in "90":
                qtile.current_window.togroup(name, switch_group=False)
                qtile.focus_screen(2)
                qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.function(go_to_group(i.name)),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.function(go_to_group_and_move_window(i.name)),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(margin = 8),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(),
]

widget_defaults = dict(
    font="mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

gB = widget.GroupBox(visible_groups=['1','2','3','4','5','6','7','8','9','0'])
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                gB,
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Pomodoro(),
                widget.NetGraph(),
                widget.OpenWeather(location="Rapid City",
                                   format='{location_city}: {temp}*C; ',
                                   update_interval=300,
                                   ),
                widget.TextBox("Welcome to the Internet, Ryott! Your Volume is at ", name="default"),
                widget.Volume(),


                widget.Clock(format="%Y-%m-%d %a %H:%M"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
# gB1 = widget.GroupBox(visible_groups=['1','2','3','4'])
# gB2 = widget.GroupBox(visible_groups=['5','6','7','8'])
# gB3 = widget.GroupBox(visible_groups=['9','0'])
# Reconfigure Screens

reconfigure_screens = True
@hook.subscribe.screens_reconfigured
async def _():
    if len(qtile.screens) == 1:
        gB1 = widget.GroupBox(visible_groups=['1','2','3','4','5','6','7','8','9','0'])

        screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB1,
                        widget.WindowName(),
                        widget.Chord(
                            chords_colors={
                                "launch": ("#ff0000", "#ffffff"),
                            },
                            name_transform=lambda name: name.upper(),
                        ),
                        widget.Pomodoro(),
                        widget.NetGraph(),
                        widget.OpenWeather(location="Rapid City",
                                           format='{location_city}: {temp}*C; ',
                                           update_interval=300,
                                           ),
                        widget.TextBox("Welcome to the Internet, Ryott! Your Volume is at ", name="default"),
                        widget.Volume(),


                        widget.Clock(format="%Y-%m-%d %a %H:%M"),
                        widget.QuickExit(),
                    ],
                    24,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            ),
        ]
    elif len(qtile.screens) == 2:
        gB1 = widget.GroupBox(visible_groups=['1','2','3','4','5'])
        gB2 = widget.GroupBox(visible_groups=['6','7','8','9','0'])

        screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB1,
                        widget.WindowName(),
                        widget.Chord(
                            chords_colors={
                                "launch": ("#ff0000", "#ffffff"),
                            },
                            name_transform=lambda name: name.upper(),
                        ),
                        widget.Pomodoro(),
                        widget.NetGraph(),
                        widget.OpenWeather(location="Rapid City",
                                           format='{location_city}: {temp}*C; ',
                                           update_interval=300,
                                           ),
                        widget.TextBox("Welcome to the Internet, Ryott! Your Volume is at ", name="default"),
                        widget.Volume(),


                        widget.Clock(format="%Y-%m-%d %a %H:%M"),
                        widget.QuickExit(),
                    ],
                    24,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            ),

            Screen(
                top = bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB2,
                        widget.Prompt(),
                        widget.WindowName(),
                        widget.CheckUpdates(
                            colour_have_updates='ff0000',
                            colour_no_updates='ffffff',
                            distro='Arch_checkupdates',
                            font='mono',
                            no_update_string='No Updates',
                            update_interval=60,
                        ),
                        widget.Spacer(length=50),
                        widget.Pomodoro(),
                        widget.Spacer(length=50),
                        widget.Clock(format="%Y-%m-%d %a %H:%M"),
                    ],
                    24,
                )
            ),
        ]
    elif len(qtile.screens) == 3:
        gB1 = widget.GroupBox(visible_groups=['1','2','3','4'])
        gB2 = widget.GroupBox(visible_groups=['5','6','7','8'])
        gB3 = widget.GroupBox(visible_groups=['9','0'])
        screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB1,
                        widget.WindowName(),
                        widget.Chord(
                            chords_colors={
                                "launch": ("#ff0000", "#ffffff"),
                            },
                            name_transform=lambda name: name.upper(),
                        ),
                        widget.Pomodoro(),
                        widget.NetGraph(),
                        widget.OpenWeather(location="Rapid City",
                                           format='{location_city}: {temp}*C; ',
                                           update_interval=300,
                                           ),
                        widget.TextBox("Welcome to the Internet, Ryott! Your Volume is at ", name="default"),
                        widget.Volume(),


                        widget.Clock(format="%Y-%m-%d %a %H:%M"),
                        widget.QuickExit(),
                    ],
                    24,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            ),

            Screen(
                top = bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB2,
                        widget.Prompt(),
                        widget.WindowName(),
                        widget.CheckUpdates(
                            colour_have_updates='ff0000',
                            colour_no_updates='ffffff',
                            distro='Arch_checkupdates',
                            font='mono',
                            no_update_string='No Updates',
                            update_interval=60,
                        ),
                        widget.Spacer(length=50),
                        widget.Pomodoro(),
                        widget.Spacer(length=50),
                        widget.Clock(format="%Y-%m-%d %a %H:%M"),
                    ],
                    24,
                )
            ),
            Screen(
                top = bar.Bar(
                    [
                        widget.CurrentLayout(),
                        gB3,
                        widget.Spacer(),
                        widget.Chord(),
                    ],
                    24),
            ),

        ]
    if hasattr(gB1, 'bar'):
        gB1.bar.draw()
    if hasattr(gB2, 'bar'):
        gB2.bar.draw()
    if hasattr(gB3, 'bar'):
        gB3.bar.draw()




# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#Startup script
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
