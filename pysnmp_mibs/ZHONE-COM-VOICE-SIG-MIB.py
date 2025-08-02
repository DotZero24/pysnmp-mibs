_n='hookFlashTimerMax'
_m='hookFlashTimerMin'
_l='sysMaxBreakPulseWidth'
_k='sysMinBreakPulseWidth'
_j='sysMaxMakePulseWidth'
_i='sysMinMakePulseWidth'
_h='sysPulseInterDigitTimer'
_g='sysCallWaitDelay'
_f='sysCallWaitMaxRepeat'
_e='sysNoResponseTimer'
_d='sysKeepAliveTimer'
_c='sysInitRetransmitTimer'
_b='sysMaxRetransmitTimer'
_a='sysDisconnectMaxTimer'
_Z='sysDisconnectMinTimer'
_Y='sysDisconnectWaitTimer'
_X='sysMaxWaitingDelay'
_W='sysMax2Enable'
_V='sysMax1Enable'
_U='sysConfigMax2'
_T='sysConfigMax1'
_S='sysServerMaxTimer'
_R='sysStutterToneTo'
_Q='sysReorderToneTo'
_P='sysRingbackTo'
_O='sysRingingTo'
_N='sysOffhookWarnToneTo'
_M='sysMsgWaitToneTo'
_L='sysDialToneTo'
_K='sysBusyToneTo'
_J='sysCriticalDialTo'
_I='sysPartialDialTo'
_H='TruthValue'
_G='Integer32'
_F='milliseconds'
_E='seconds'
_D='Unsigned32'
_C='read-write'
_B='ZHONE-COM-VOICE-SIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
zhoneVoice,=mibBuilder.importSymbols('Zhone','zhoneVoice')
zhoneVoiceSignalingMib=ModuleIdentity((1,3,6,1,4,1,5504,4,3,7))
if mibBuilder.loadTexts:zhoneVoiceSignalingMib.setRevisions(('2004-10-21 14:51','2000-10-10 18:05'))
_ZhoneVoiceSignalingTimers_ObjectIdentity=ObjectIdentity
zhoneVoiceSignalingTimers=_ZhoneVoiceSignalingTimers_ObjectIdentity((1,3,6,1,4,1,5504,4,3,7,1))
if mibBuilder.loadTexts:zhoneVoiceSignalingTimers.setStatus(_A)
class _HookFlashTimerMin_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HookFlashTimerMin_Type.__name__=_G
_HookFlashTimerMin_Object=MibScalar
hookFlashTimerMin=_HookFlashTimerMin_Object((1,3,6,1,4,1,5504,4,3,7,1,1),_HookFlashTimerMin_Type())
hookFlashTimerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hookFlashTimerMin.setStatus(_A)
class _HookFlashTimerMax_Type(Integer32):defaultValue=1550;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HookFlashTimerMax_Type.__name__=_G
_HookFlashTimerMax_Object=MibScalar
hookFlashTimerMax=_HookFlashTimerMax_Object((1,3,6,1,4,1,5504,4,3,7,1,2),_HookFlashTimerMax_Type())
hookFlashTimerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hookFlashTimerMax.setStatus(_A)
class _SysPartialDialTo_Type(Unsigned32):defaultValue=16
_SysPartialDialTo_Type.__name__=_D
_SysPartialDialTo_Object=MibScalar
sysPartialDialTo=_SysPartialDialTo_Object((1,3,6,1,4,1,5504,4,3,7,1,3),_SysPartialDialTo_Type())
sysPartialDialTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPartialDialTo.setStatus(_A)
if mibBuilder.loadTexts:sysPartialDialTo.setUnits(_E)
class _SysCriticalDialTo_Type(Unsigned32):defaultValue=4
_SysCriticalDialTo_Type.__name__=_D
_SysCriticalDialTo_Object=MibScalar
sysCriticalDialTo=_SysCriticalDialTo_Object((1,3,6,1,4,1,5504,4,3,7,1,4),_SysCriticalDialTo_Type())
sysCriticalDialTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCriticalDialTo.setStatus(_A)
if mibBuilder.loadTexts:sysCriticalDialTo.setUnits(_E)
class _SysBusyToneTo_Type(Unsigned32):defaultValue=30
_SysBusyToneTo_Type.__name__=_D
_SysBusyToneTo_Object=MibScalar
sysBusyToneTo=_SysBusyToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,5),_SysBusyToneTo_Type())
sysBusyToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBusyToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysBusyToneTo.setUnits(_E)
class _SysDialToneTo_Type(Unsigned32):defaultValue=16
_SysDialToneTo_Type.__name__=_D
_SysDialToneTo_Object=MibScalar
sysDialToneTo=_SysDialToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,6),_SysDialToneTo_Type())
sysDialToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDialToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysDialToneTo.setUnits(_E)
class _SysMsgWaitToneTo_Type(Unsigned32):defaultValue=16
_SysMsgWaitToneTo_Type.__name__=_D
_SysMsgWaitToneTo_Object=MibScalar
sysMsgWaitToneTo=_SysMsgWaitToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,7),_SysMsgWaitToneTo_Type())
sysMsgWaitToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMsgWaitToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysMsgWaitToneTo.setUnits(_E)
class _SysOffhookWarnToneTo_Type(Unsigned32):defaultValue=0
_SysOffhookWarnToneTo_Type.__name__=_D
_SysOffhookWarnToneTo_Object=MibScalar
sysOffhookWarnToneTo=_SysOffhookWarnToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,8),_SysOffhookWarnToneTo_Type())
sysOffhookWarnToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysOffhookWarnToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysOffhookWarnToneTo.setUnits(_E)
class _SysRingingTo_Type(Unsigned32):defaultValue=180
_SysRingingTo_Type.__name__=_D
_SysRingingTo_Object=MibScalar
sysRingingTo=_SysRingingTo_Object((1,3,6,1,4,1,5504,4,3,7,1,9),_SysRingingTo_Type())
sysRingingTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysRingingTo.setStatus(_A)
if mibBuilder.loadTexts:sysRingingTo.setUnits(_E)
class _SysRingbackTo_Type(Unsigned32):defaultValue=180
_SysRingbackTo_Type.__name__=_D
_SysRingbackTo_Object=MibScalar
sysRingbackTo=_SysRingbackTo_Object((1,3,6,1,4,1,5504,4,3,7,1,10),_SysRingbackTo_Type())
sysRingbackTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysRingbackTo.setStatus(_A)
if mibBuilder.loadTexts:sysRingbackTo.setUnits(_E)
class _SysReorderToneTo_Type(Unsigned32):defaultValue=30
_SysReorderToneTo_Type.__name__=_D
_SysReorderToneTo_Object=MibScalar
sysReorderToneTo=_SysReorderToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,11),_SysReorderToneTo_Type())
sysReorderToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysReorderToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysReorderToneTo.setUnits(_E)
class _SysStutterToneTo_Type(Unsigned32):defaultValue=16
_SysStutterToneTo_Type.__name__=_D
_SysStutterToneTo_Object=MibScalar
sysStutterToneTo=_SysStutterToneTo_Object((1,3,6,1,4,1,5504,4,3,7,1,12),_SysStutterToneTo_Type())
sysStutterToneTo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysStutterToneTo.setStatus(_A)
if mibBuilder.loadTexts:sysStutterToneTo.setUnits(_E)
class _SysServerMaxTimer_Type(Unsigned32):defaultValue=20
_SysServerMaxTimer_Type.__name__=_D
_SysServerMaxTimer_Object=MibScalar
sysServerMaxTimer=_SysServerMaxTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,13),_SysServerMaxTimer_Type())
sysServerMaxTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysServerMaxTimer.setStatus(_A)
class _SysConfigMax1_Type(Unsigned32):defaultValue=5
_SysConfigMax1_Type.__name__=_D
_SysConfigMax1_Object=MibScalar
sysConfigMax1=_SysConfigMax1_Object((1,3,6,1,4,1,5504,4,3,7,1,14),_SysConfigMax1_Type())
sysConfigMax1.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigMax1.setStatus(_A)
class _SysConfigMax2_Type(Unsigned32):defaultValue=7
_SysConfigMax2_Type.__name__=_D
_SysConfigMax2_Object=MibScalar
sysConfigMax2=_SysConfigMax2_Object((1,3,6,1,4,1,5504,4,3,7,1,15),_SysConfigMax2_Type())
sysConfigMax2.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigMax2.setStatus(_A)
class _SysMax1Enable_Type(TruthValue):defaultValue=1
_SysMax1Enable_Type.__name__=_H
_SysMax1Enable_Object=MibScalar
sysMax1Enable=_SysMax1Enable_Object((1,3,6,1,4,1,5504,4,3,7,1,16),_SysMax1Enable_Type())
sysMax1Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMax1Enable.setStatus(_A)
class _SysMax2Enable_Type(TruthValue):defaultValue=1
_SysMax2Enable_Type.__name__=_H
_SysMax2Enable_Object=MibScalar
sysMax2Enable=_SysMax2Enable_Object((1,3,6,1,4,1,5504,4,3,7,1,17),_SysMax2Enable_Type())
sysMax2Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMax2Enable.setStatus(_A)
class _SysMaxWaitingDelay_Type(Unsigned32):defaultValue=600
_SysMaxWaitingDelay_Type.__name__=_D
_SysMaxWaitingDelay_Object=MibScalar
sysMaxWaitingDelay=_SysMaxWaitingDelay_Object((1,3,6,1,4,1,5504,4,3,7,1,18),_SysMaxWaitingDelay_Type())
sysMaxWaitingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMaxWaitingDelay.setStatus(_A)
if mibBuilder.loadTexts:sysMaxWaitingDelay.setUnits(_E)
class _SysDisconnectWaitTimer_Type(Unsigned32):defaultValue=15
_SysDisconnectWaitTimer_Type.__name__=_D
_SysDisconnectWaitTimer_Object=MibScalar
sysDisconnectWaitTimer=_SysDisconnectWaitTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,19),_SysDisconnectWaitTimer_Type())
sysDisconnectWaitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDisconnectWaitTimer.setStatus(_A)
if mibBuilder.loadTexts:sysDisconnectWaitTimer.setUnits(_E)
class _SysDisconnectMinTimer_Type(Unsigned32):defaultValue=15
_SysDisconnectMinTimer_Type.__name__=_D
_SysDisconnectMinTimer_Object=MibScalar
sysDisconnectMinTimer=_SysDisconnectMinTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,20),_SysDisconnectMinTimer_Type())
sysDisconnectMinTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDisconnectMinTimer.setStatus(_A)
if mibBuilder.loadTexts:sysDisconnectMinTimer.setUnits(_E)
class _SysDisconnectMaxTimer_Type(Unsigned32):defaultValue=600
_SysDisconnectMaxTimer_Type.__name__=_D
_SysDisconnectMaxTimer_Object=MibScalar
sysDisconnectMaxTimer=_SysDisconnectMaxTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,21),_SysDisconnectMaxTimer_Type())
sysDisconnectMaxTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDisconnectMaxTimer.setStatus(_A)
if mibBuilder.loadTexts:sysDisconnectMaxTimer.setUnits(_E)
class _SysMaxRetransmitTimer_Type(Unsigned32):defaultValue=4
_SysMaxRetransmitTimer_Type.__name__=_D
_SysMaxRetransmitTimer_Object=MibScalar
sysMaxRetransmitTimer=_SysMaxRetransmitTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,22),_SysMaxRetransmitTimer_Type())
sysMaxRetransmitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMaxRetransmitTimer.setStatus(_A)
if mibBuilder.loadTexts:sysMaxRetransmitTimer.setUnits(_E)
class _SysInitRetransmitTimer_Type(Unsigned32):defaultValue=200
_SysInitRetransmitTimer_Type.__name__=_D
_SysInitRetransmitTimer_Object=MibScalar
sysInitRetransmitTimer=_SysInitRetransmitTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,23),_SysInitRetransmitTimer_Type())
sysInitRetransmitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysInitRetransmitTimer.setStatus(_A)
if mibBuilder.loadTexts:sysInitRetransmitTimer.setUnits(_F)
class _SysKeepAliveTimer_Type(Unsigned32):defaultValue=60
_SysKeepAliveTimer_Type.__name__=_D
_SysKeepAliveTimer_Object=MibScalar
sysKeepAliveTimer=_SysKeepAliveTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,24),_SysKeepAliveTimer_Type())
sysKeepAliveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysKeepAliveTimer.setStatus(_A)
if mibBuilder.loadTexts:sysKeepAliveTimer.setUnits('minutes')
class _SysNoResponseTimer_Type(Unsigned32):defaultValue=30
_SysNoResponseTimer_Type.__name__=_D
_SysNoResponseTimer_Object=MibScalar
sysNoResponseTimer=_SysNoResponseTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,25),_SysNoResponseTimer_Type())
sysNoResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysNoResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:sysNoResponseTimer.setUnits(_E)
class _SysCallWaitMaxRepeat_Type(Unsigned32):defaultValue=2
_SysCallWaitMaxRepeat_Type.__name__=_D
_SysCallWaitMaxRepeat_Object=MibScalar
sysCallWaitMaxRepeat=_SysCallWaitMaxRepeat_Object((1,3,6,1,4,1,5504,4,3,7,1,26),_SysCallWaitMaxRepeat_Type())
sysCallWaitMaxRepeat.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCallWaitMaxRepeat.setStatus(_A)
class _SysCallWaitDelay_Type(Unsigned32):defaultValue=10
_SysCallWaitDelay_Type.__name__=_D
_SysCallWaitDelay_Object=MibScalar
sysCallWaitDelay=_SysCallWaitDelay_Object((1,3,6,1,4,1,5504,4,3,7,1,27),_SysCallWaitDelay_Type())
sysCallWaitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCallWaitDelay.setStatus(_A)
if mibBuilder.loadTexts:sysCallWaitDelay.setUnits(_E)
class _SysPulseInterDigitTimer_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1500))
_SysPulseInterDigitTimer_Type.__name__=_D
_SysPulseInterDigitTimer_Object=MibScalar
sysPulseInterDigitTimer=_SysPulseInterDigitTimer_Object((1,3,6,1,4,1,5504,4,3,7,1,28),_SysPulseInterDigitTimer_Type())
sysPulseInterDigitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPulseInterDigitTimer.setStatus(_A)
if mibBuilder.loadTexts:sysPulseInterDigitTimer.setUnits(_F)
class _SysMinMakePulseWidth_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_SysMinMakePulseWidth_Type.__name__=_D
_SysMinMakePulseWidth_Object=MibScalar
sysMinMakePulseWidth=_SysMinMakePulseWidth_Object((1,3,6,1,4,1,5504,4,3,7,1,29),_SysMinMakePulseWidth_Type())
sysMinMakePulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMinMakePulseWidth.setStatus(_A)
if mibBuilder.loadTexts:sysMinMakePulseWidth.setUnits(_F)
class _SysMaxMakePulseWidth_Type(Unsigned32):defaultValue=55;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_SysMaxMakePulseWidth_Type.__name__=_D
_SysMaxMakePulseWidth_Object=MibScalar
sysMaxMakePulseWidth=_SysMaxMakePulseWidth_Object((1,3,6,1,4,1,5504,4,3,7,1,30),_SysMaxMakePulseWidth_Type())
sysMaxMakePulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMaxMakePulseWidth.setStatus(_A)
if mibBuilder.loadTexts:sysMaxMakePulseWidth.setUnits(_F)
class _SysMinBreakPulseWidth_Type(Unsigned32):defaultValue=45;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_SysMinBreakPulseWidth_Type.__name__=_D
_SysMinBreakPulseWidth_Object=MibScalar
sysMinBreakPulseWidth=_SysMinBreakPulseWidth_Object((1,3,6,1,4,1,5504,4,3,7,1,31),_SysMinBreakPulseWidth_Type())
sysMinBreakPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMinBreakPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:sysMinBreakPulseWidth.setUnits(_F)
class _SysMaxBreakPulseWidth_Type(Unsigned32):defaultValue=75;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_SysMaxBreakPulseWidth_Type.__name__=_D
_SysMaxBreakPulseWidth_Object=MibScalar
sysMaxBreakPulseWidth=_SysMaxBreakPulseWidth_Object((1,3,6,1,4,1,5504,4,3,7,1,32),_SysMaxBreakPulseWidth_Type())
sysMaxBreakPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMaxBreakPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:sysMaxBreakPulseWidth.setUnits(_F)
zhoneVoiceSignalingObjectsGroup=ObjectGroup((1,3,6,1,4,1,5504,4,3,7,1,33))
zhoneVoiceSignalingObjectsGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:zhoneVoiceSignalingObjectsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhoneVoiceSignalingMib':zhoneVoiceSignalingMib,'zhoneVoiceSignalingTimers':zhoneVoiceSignalingTimers,_m:hookFlashTimerMin,_n:hookFlashTimerMax,_I:sysPartialDialTo,_J:sysCriticalDialTo,_K:sysBusyToneTo,_L:sysDialToneTo,_M:sysMsgWaitToneTo,_N:sysOffhookWarnToneTo,_O:sysRingingTo,_P:sysRingbackTo,_Q:sysReorderToneTo,_R:sysStutterToneTo,_S:sysServerMaxTimer,_T:sysConfigMax1,_U:sysConfigMax2,_V:sysMax1Enable,_W:sysMax2Enable,_X:sysMaxWaitingDelay,_Y:sysDisconnectWaitTimer,_Z:sysDisconnectMinTimer,_a:sysDisconnectMaxTimer,_b:sysMaxRetransmitTimer,_c:sysInitRetransmitTimer,_d:sysKeepAliveTimer,_e:sysNoResponseTimer,_f:sysCallWaitMaxRepeat,_g:sysCallWaitDelay,_h:sysPulseInterDigitTimer,_i:sysMinMakePulseWidth,_j:sysMaxMakePulseWidth,_k:sysMinBreakPulseWidth,_l:sysMaxBreakPulseWidth,'zhoneVoiceSignalingObjectsGroup':zhoneVoiceSignalingObjectsGroup})