pwr_hist = {}
ax_seg_pf = {}


def looping(var, data, name):
    for item in range(len(data)):
        var[name+'_'+str(item+1)] = data[item]


def create_pf(pf_list):
    looping(ax_seg_pf, pf_list, 'ax_seg')


def create_time_hist(time_list):
    looping(pwr_hist, time_list, 'time')


def create_bu_hist(burnup_list):
    looping(pwr_hist, burnup_list, 'burnup')


def create_lhr_hist(lhr_list):
    looping(pwr_hist, lhr_list, 'lhr')


def create_cooltemp_hist(cooltemp_list):
    looping(pwr_hist, cooltemp_list, 'coolTemp')


def create_coolpress_hist(coolpress_list):
    looping(pwr_hist, coolpress_list, 'coolPress')


def create_nflux_hist(nflux_list):
    looping(pwr_hist, nflux_list, 'nflux')


def create_coolvelocity_hist(coolvelocity_list):
    looping(pwr_hist, coolvelocity_list, 'coolVelocity')


def create_iPrint_opt(iPrint_list):
    looping(pwr_hist, iPrint_list, 'iPrint opt')


def create_iState_opt(iState_list):
    looping(pwr_hist, iState_list, 'iState opt')


def create_iTime_opt(iTime_list):
    looping(pwr_hist, iTime_list, 'iTime opt')
