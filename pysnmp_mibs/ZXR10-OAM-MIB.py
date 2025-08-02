_J='DisplayString'
_I='ifIndex'
_H='IF-MIB'
_G='read-only'
_F='enable'
_E='disnable'
_D='Integer32'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10switch_ObjectIdentity=ObjectIdentity
zxr10switch=_Zxr10switch_ObjectIdentity((1,3,6,1,4,1,3902,3,102))
_Zxr10ethernetOam_ObjectIdentity=ObjectIdentity
zxr10ethernetOam=_Zxr10ethernetOam_ObjectIdentity((1,3,6,1,4,1,3902,3,102,20))
_Zxr10ethernetOamGlobalConfig_ObjectIdentity=ObjectIdentity
zxr10ethernetOamGlobalConfig=_Zxr10ethernetOamGlobalConfig_ObjectIdentity((1,3,6,1,4,1,3902,3,102,20,1))
class _Zxr10ethernetOamGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Zxr10ethernetOamGlobalEnable_Type.__name__=_D
_Zxr10ethernetOamGlobalEnable_Object=MibScalar
zxr10ethernetOamGlobalEnable=_Zxr10ethernetOamGlobalEnable_Object((1,3,6,1,4,1,3902,3,102,20,1,1),_Zxr10ethernetOamGlobalEnable_Type())
zxr10ethernetOamGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamGlobalEnable.setStatus(_A)
class _Zxr10ethernetOamOuiInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,3))
_Zxr10ethernetOamOuiInformation_Type.__name__=_J
_Zxr10ethernetOamOuiInformation_Object=MibScalar
zxr10ethernetOamOuiInformation=_Zxr10ethernetOamOuiInformation_Object((1,3,6,1,4,1,3902,3,102,20,1,2),_Zxr10ethernetOamOuiInformation_Type())
zxr10ethernetOamOuiInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamOuiInformation.setStatus(_A)
class _Zxr10ethernetOamRemoteLoopbackTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Zxr10ethernetOamRemoteLoopbackTimeout_Type.__name__=_C
_Zxr10ethernetOamRemoteLoopbackTimeout_Object=MibScalar
zxr10ethernetOamRemoteLoopbackTimeout=_Zxr10ethernetOamRemoteLoopbackTimeout_Object((1,3,6,1,4,1,3902,3,102,20,1,3),_Zxr10ethernetOamRemoteLoopbackTimeout_Type())
zxr10ethernetOamRemoteLoopbackTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamRemoteLoopbackTimeout.setStatus(_A)
_Zxr10ethernetOamIfConfigTable_Object=MibTable
zxr10ethernetOamIfConfigTable=_Zxr10ethernetOamIfConfigTable_Object((1,3,6,1,4,1,3902,3,102,20,2))
if mibBuilder.loadTexts:zxr10ethernetOamIfConfigTable.setStatus(_A)
_Zxr10ethernetOamIfConfigEntry_Object=MibTableRow
zxr10ethernetOamIfConfigEntry=_Zxr10ethernetOamIfConfigEntry_Object((1,3,6,1,4,1,3902,3,102,20,2,1))
zxr10ethernetOamIfConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxr10ethernetOamIfConfigEntry.setStatus(_A)
class _Zxr10ethernetOamIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Zxr10ethernetOamIfEnable_Type.__name__=_D
_Zxr10ethernetOamIfEnable_Object=MibTableColumn
zxr10ethernetOamIfEnable=_Zxr10ethernetOamIfEnable_Object((1,3,6,1,4,1,3902,3,102,20,2,1,1),_Zxr10ethernetOamIfEnable_Type())
zxr10ethernetOamIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamIfEnable.setStatus(_A)
class _Zxr10ethernetOamRemoteLoopbackEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Zxr10ethernetOamRemoteLoopbackEnable_Type.__name__=_D
_Zxr10ethernetOamRemoteLoopbackEnable_Object=MibTableColumn
zxr10ethernetOamRemoteLoopbackEnable=_Zxr10ethernetOamRemoteLoopbackEnable_Object((1,3,6,1,4,1,3902,3,102,20,2,1,2),_Zxr10ethernetOamRemoteLoopbackEnable_Type())
zxr10ethernetOamRemoteLoopbackEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamRemoteLoopbackEnable.setStatus(_A)
class _Zxr10ethernetOamifperiod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Zxr10ethernetOamifperiod_Type.__name__=_C
_Zxr10ethernetOamifperiod_Object=MibTableColumn
zxr10ethernetOamifperiod=_Zxr10ethernetOamifperiod_Object((1,3,6,1,4,1,3902,3,102,20,2,1,3),_Zxr10ethernetOamifperiod_Type())
zxr10ethernetOamifperiod.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifperiod.setStatus(_A)
class _Zxr10ethernetOamifmode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Zxr10ethernetOamifmode_Type.__name__=_C
_Zxr10ethernetOamifmode_Object=MibTableColumn
zxr10ethernetOamifmode=_Zxr10ethernetOamifmode_Object((1,3,6,1,4,1,3902,3,102,20,2,1,4),_Zxr10ethernetOamifmode_Type())
zxr10ethernetOamifmode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifmode.setStatus(_A)
class _Zxr10ethernetOamiftimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,20))
_Zxr10ethernetOamiftimeout_Type.__name__=_C
_Zxr10ethernetOamiftimeout_Object=MibTableColumn
zxr10ethernetOamiftimeout=_Zxr10ethernetOamiftimeout_Object((1,3,6,1,4,1,3902,3,102,20,2,1,5),_Zxr10ethernetOamiftimeout_Type())
zxr10ethernetOamiftimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamiftimeout.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Zxr10ethernetOamifLinkMonitorEnable_Type.__name__=_D
_Zxr10ethernetOamifLinkMonitorEnable_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorEnable=_Zxr10ethernetOamifLinkMonitorEnable_Object((1,3,6,1,4,1,3902,3,102,20,2,1,6),_Zxr10ethernetOamifLinkMonitorEnable_Type())
zxr10ethernetOamifLinkMonitorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorEnable.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold=_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Object((1,3,6,1,4,1,3902,3,102,20,2,1,7),_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type())
zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorSymbolPeriodwindow=_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Object((1,3,6,1,4,1,3902,3,102,20,2,1,8),_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type())
zxr10ethernetOamifLinkMonitorSymbolPeriodwindow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorSymbolPeriodwindow.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFramethreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10ethernetOamifLinkMonitorFramethreshold_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFramethreshold_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFramethreshold=_Zxr10ethernetOamifLinkMonitorFramethreshold_Object((1,3,6,1,4,1,3902,3,102,20,2,1,9),_Zxr10ethernetOamifLinkMonitorFramethreshold_Type())
zxr10ethernetOamifLinkMonitorFramethreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFramethreshold.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFramewindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Zxr10ethernetOamifLinkMonitorFramewindow_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFramewindow_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFramewindow=_Zxr10ethernetOamifLinkMonitorFramewindow_Object((1,3,6,1,4,1,3902,3,102,20,2,1,10),_Zxr10ethernetOamifLinkMonitorFramewindow_Type())
zxr10ethernetOamifLinkMonitorFramewindow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFramewindow.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFramePeriodthreshold=_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Object((1,3,6,1,4,1,3902,3,102,20,2,1,11),_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type())
zxr10ethernetOamifLinkMonitorFramePeriodthreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFramePeriodthreshold.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600000))
_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFramePeriodwindow=_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Object((1,3,6,1,4,1,3902,3,102,20,2,1,12),_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type())
zxr10ethernetOamifLinkMonitorFramePeriodwindow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFramePeriodwindow.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFrameSecondsthreshold=_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Object((1,3,6,1,4,1,3902,3,102,20,2,1,13),_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type())
zxr10ethernetOamifLinkMonitorFrameSecondsthreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFrameSecondsthreshold.setStatus(_A)
class _Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,900))
_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type.__name__=_C
_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Object=MibTableColumn
zxr10ethernetOamifLinkMonitorFrameSecondswindow=_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Object((1,3,6,1,4,1,3902,3,102,20,2,1,14),_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type())
zxr10ethernetOamifLinkMonitorFrameSecondswindow.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ethernetOamifLinkMonitorFrameSecondswindow.setStatus(_A)
_Zxr10ethernetOamifName_Type=DisplayString
_Zxr10ethernetOamifName_Object=MibTableColumn
zxr10ethernetOamifName=_Zxr10ethernetOamifName_Object((1,3,6,1,4,1,3902,3,102,20,2,1,15),_Zxr10ethernetOamifName_Type())
zxr10ethernetOamifName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxr10ethernetOamifName.setStatus(_A)
_Zxr10ethernetOamShowTable_Object=MibTable
zxr10ethernetOamShowTable=_Zxr10ethernetOamShowTable_Object((1,3,6,1,4,1,3902,3,102,20,3))
if mibBuilder.loadTexts:zxr10ethernetOamShowTable.setStatus(_A)
_Zxr10ethernetOamShowEntry_Object=MibTableRow
zxr10ethernetOamShowEntry=_Zxr10ethernetOamShowEntry_Object((1,3,6,1,4,1,3902,3,102,20,3,1))
zxr10ethernetOamShowEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxr10ethernetOamShowEntry.setStatus(_A)
_Zxr10ethernetOamShowDiscovery_Type=DisplayString
_Zxr10ethernetOamShowDiscovery_Object=MibTableColumn
zxr10ethernetOamShowDiscovery=_Zxr10ethernetOamShowDiscovery_Object((1,3,6,1,4,1,3902,3,102,20,3,1,1),_Zxr10ethernetOamShowDiscovery_Type())
zxr10ethernetOamShowDiscovery.setMaxAccess(_G)
if mibBuilder.loadTexts:zxr10ethernetOamShowDiscovery.setStatus(_A)
_Zxr10ethernetOamShowLinkMonitor_Type=DisplayString
_Zxr10ethernetOamShowLinkMonitor_Object=MibTableColumn
zxr10ethernetOamShowLinkMonitor=_Zxr10ethernetOamShowLinkMonitor_Object((1,3,6,1,4,1,3902,3,102,20,3,1,2),_Zxr10ethernetOamShowLinkMonitor_Type())
zxr10ethernetOamShowLinkMonitor.setMaxAccess(_G)
if mibBuilder.loadTexts:zxr10ethernetOamShowLinkMonitor.setStatus(_A)
_Zxr10ethernetOamShowStatistics_Type=DisplayString
_Zxr10ethernetOamShowStatistics_Object=MibTableColumn
zxr10ethernetOamShowStatistics=_Zxr10ethernetOamShowStatistics_Object((1,3,6,1,4,1,3902,3,102,20,3,1,3),_Zxr10ethernetOamShowStatistics_Type())
zxr10ethernetOamShowStatistics.setMaxAccess(_G)
if mibBuilder.loadTexts:zxr10ethernetOamShowStatistics.setStatus(_A)
mibBuilder.exportSymbols('ZXR10-OAM-MIB',**{_J:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10switch':zxr10switch,'zxr10ethernetOam':zxr10ethernetOam,'zxr10ethernetOamGlobalConfig':zxr10ethernetOamGlobalConfig,'zxr10ethernetOamGlobalEnable':zxr10ethernetOamGlobalEnable,'zxr10ethernetOamOuiInformation':zxr10ethernetOamOuiInformation,'zxr10ethernetOamRemoteLoopbackTimeout':zxr10ethernetOamRemoteLoopbackTimeout,'zxr10ethernetOamIfConfigTable':zxr10ethernetOamIfConfigTable,'zxr10ethernetOamIfConfigEntry':zxr10ethernetOamIfConfigEntry,'zxr10ethernetOamIfEnable':zxr10ethernetOamIfEnable,'zxr10ethernetOamRemoteLoopbackEnable':zxr10ethernetOamRemoteLoopbackEnable,'zxr10ethernetOamifperiod':zxr10ethernetOamifperiod,'zxr10ethernetOamifmode':zxr10ethernetOamifmode,'zxr10ethernetOamiftimeout':zxr10ethernetOamiftimeout,'zxr10ethernetOamifLinkMonitorEnable':zxr10ethernetOamifLinkMonitorEnable,'zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold':zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold,'zxr10ethernetOamifLinkMonitorSymbolPeriodwindow':zxr10ethernetOamifLinkMonitorSymbolPeriodwindow,'zxr10ethernetOamifLinkMonitorFramethreshold':zxr10ethernetOamifLinkMonitorFramethreshold,'zxr10ethernetOamifLinkMonitorFramewindow':zxr10ethernetOamifLinkMonitorFramewindow,'zxr10ethernetOamifLinkMonitorFramePeriodthreshold':zxr10ethernetOamifLinkMonitorFramePeriodthreshold,'zxr10ethernetOamifLinkMonitorFramePeriodwindow':zxr10ethernetOamifLinkMonitorFramePeriodwindow,'zxr10ethernetOamifLinkMonitorFrameSecondsthreshold':zxr10ethernetOamifLinkMonitorFrameSecondsthreshold,'zxr10ethernetOamifLinkMonitorFrameSecondswindow':zxr10ethernetOamifLinkMonitorFrameSecondswindow,'zxr10ethernetOamifName':zxr10ethernetOamifName,'zxr10ethernetOamShowTable':zxr10ethernetOamShowTable,'zxr10ethernetOamShowEntry':zxr10ethernetOamShowEntry,'zxr10ethernetOamShowDiscovery':zxr10ethernetOamShowDiscovery,'zxr10ethernetOamShowLinkMonitor':zxr10ethernetOamShowLinkMonitor,'zxr10ethernetOamShowStatistics':zxr10ethernetOamShowStatistics})