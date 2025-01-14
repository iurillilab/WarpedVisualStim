# -*- coding: utf-8 -*-
"""
Example script to test StimulusRoutines.CombinedStimuli class
"""

import matplotlib.pyplot as plt
import WarpedVisualStim.StimulusRoutines as stim
from WarpedVisualStim.MonitorSetup import Monitor, Indicator
from WarpedVisualStim.DisplayStimulus import DisplaySequence

# ============================ monitor setup ======================================
mon_resolution = (1080, 1920)  # enter your monitors resolution
mon_width_cm = 52.  # enter your monitors width in cm
mon_height_cm = 29.  # enter your monitors height in cm
mon_refresh_rate = 60  # enter your monitors height in Hz
mon_C2T_cm = mon_height_cm / 2.
mon_C2A_cm = mon_width_cm / 2.
mon_center_coordinates = (0., 60.)
mon_dis = 13.5
mon_downsample_rate = 5
# =================================================================================

# ============================ indicator setup ====================================
ind_width_cm = 1.
ind_height_cm = 1.
ind_position = 'southeast'
ind_is_sync = True
ind_freq = 1.
# =================================================================================

# ============================ DisplaySequence ====================================
ds_log_dir = r'E:\paola\data'
ds_backupdir = None
ds_identifier = 'TEST_triggered'
ds_display_iter = 1.
ds_mouse_id = 'MOUSE'
ds_user_id = 'PP'
ds_psychopy_mon = 'testMonitor'
ds_is_by_index = False
ds_is_interpolate = False
ds_is_triggered = True
ds_is_save_sequence = True
ds_trigger_event = "positive_edge"
ds_trigger_NI_dev = 'Dev6'
ds_trigger_NI_port = 0
ds_trigger_NI_line = 0
ds_is_sync_pulse = False
ds_sync_pulse_NI_dev = 'Dev4'
ds_sync_pulse_NI_port = 1
ds_sync_pulse_NI_line = 1
ds_display_screen = 1  #0 for display 1, 1 for display 2
ds_initial_background_color = 0.
ds_color_weights = (1., 1., 1.)
# =================================================================================

# ============================ generic stimulus parameters ========================
pregap_dur = 2.
postgap_dur = 3.
background = 0.
coordinate = 'degree'
# =================================================================================

# ============================ KSstimAllDir ====================================
ks_square_size = 25.
ks_square_center = (10, 0)
ks_flicker_frame = 10 #10 with 60fps is 6 Hz
ks_sweep_width = 20.
ks_step_width = 0.15  #0.15 gives me about 9 deg\sec of bar sweeping
ks_sweep_frame = 1
ks_iteration = 1
# =================================================================================

# ================ Initialize the monitor object ==================================
mon = Monitor(resolution=mon_resolution, dis=mon_dis, mon_width_cm=mon_width_cm,
              mon_height_cm=mon_height_cm, C2T_cm=mon_C2T_cm, C2A_cm=mon_C2A_cm,
              center_coordinates=mon_center_coordinates,
              downsample_rate=mon_downsample_rate)
# mon.plot_map()
# plt.show()
# =================================================================================

# ================ Initialize the indicator object ================================
ind = Indicator(mon, width_cm=ind_width_cm, height_cm=ind_height_cm,
                position=ind_position, is_sync=ind_is_sync, freq=ind_freq)
# =================================================================================

# ========================== KSstimAllDir =====================================
ks = stim.KSstimAllDir(monitor=mon, indicator=ind, pregap_dur=pregap_dur, postgap_dur=postgap_dur,
                       background=background, coordinate=coordinate, square_size=ks_square_size,
                       square_center=ks_square_center, flicker_frame=ks_flicker_frame,
                       sweep_width=ks_sweep_width, step_width=ks_step_width, sweep_frame=ks_sweep_frame,
                       iteration=ks_iteration)
# =================================================================================

# ================ Initialize the DisplaySequence object ==========================
ds = DisplaySequence(log_dir=ds_log_dir, backupdir=ds_backupdir,
                     identifier=ds_identifier, display_iter=ds_display_iter,
                     mouse_id=ds_mouse_id, user_id=ds_user_id,
                     psychopy_mon=ds_psychopy_mon, is_by_index=ds_is_by_index,
                     is_interpolate=ds_is_interpolate, is_triggered=ds_is_triggered,
                     trigger_event=ds_trigger_event, trigger_NI_dev=ds_trigger_NI_dev,
                     trigger_NI_port=ds_trigger_NI_port, trigger_NI_line=ds_trigger_NI_line,
                     is_sync_pulse=ds_is_sync_pulse, sync_pulse_NI_dev=ds_sync_pulse_NI_dev,
                     sync_pulse_NI_port=ds_sync_pulse_NI_port,
                     sync_pulse_NI_line=ds_sync_pulse_NI_line,
                     display_screen=ds_display_screen, is_save_sequence=ds_is_save_sequence,
                     initial_background_color=ds_initial_background_color,
                     color_weights=ds_color_weights)
# =================================================================================

# =============================== display =========================================
ds.set_stim(ks)
ds.trigger_display()
# plt.show()  #commented by PP
# =================================================================================
