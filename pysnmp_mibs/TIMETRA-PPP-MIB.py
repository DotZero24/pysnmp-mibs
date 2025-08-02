_AC='tmnxPppCompressionGroup'
_AB='tmnxPppGroup'
_AA='tmnxPppLoopbackClear'
_A9='tmnxPppLoopback'
_A8='tmnxPppLqmFailure'
_A7='tmnxPppKeepaliveFailure'
_A6='tmnxPppNcpDown'
_A5='tmnxPppNcpUp'
_A4='tmnxPppCpUp'
_A3='tmnxPppHdrCompression'
_A2='tmnxPppRemoteIPv6Address'
_A1='tmnxPppRemoteIPv6AddressType'
_A0='tmnxPppLocalIPv6Address'
_z='tmnxPppLocalIPv6AddressType'
_y='tmnxPppCpProtocol'
_x='percent'
_w='seconds'
_v='tmnxPpp7750V4v0Group'
_u='tmnxPpp7450V4v0Group'
_t='tmnxPppCpDown'
_s='tmnxPppRemoteIPv4Address'
_r='tmnxPppRemoteIPv4AddressType'
_q='tmnxPppLocalIPv4Address'
_p='tmnxPppLocalIPv4AddressType'
_o='tmnxPppRemoteAddress'
_n='tmnxPppLocalAddress'
_m='tmnxPortPortID'
_l='TIMETRA-PORT-MIB'
_k='tmnxChassisIndex'
_j='TIMETRA-CHASSIS-MIB'
_i='Gauge32'
_h='tmnxPppCpLastClearedTime'
_g='tmnxPppCpRestartCount'
_f='tmnxPppCpLastChange'
_e='tmnxPppLqmTimeDropLink'
_d='tmnxPppLqmOutPktCount'
_c='tmnxPppLqmInPktCount'
_b='tmnxPppLqmThresholdExceedsCount'
_a='tmnxPppLqmLastClearedTime'
_Z='tmnxPppLqmOperPeriod'
_Y='tmnxPppKaTimeDropLink'
_X='tmnxPppKaOutPktCount'
_W='tmnxPppKaInPktCount'
_V='tmnxPppKaThresholdExceedsCount'
_U='tmnxPppKaLastClearedTime'
_T='tmnxPppKaDropCount'
_S='tmnxPppLineMonitorMethod'
_R='tmnxPppRemoteMacAddress'
_Q='tmnxPppLinkPhase'
_P='read-write'
_O='Integer32'
_N='tmnxPppLqmOutRate'
_M='tmnxPppLqmInRate'
_L='tmnxPppQuality'
_K='tmnxPppKaPeriod'
_J='Unsigned32'
_I='InetAddress'
_H='tmnxPppNotificationGroup'
_G='tmnxPppRemoteMagicNumber'
_F='tmnxPppLocalMagicNumber'
_E='obsolete'
_D='tmnxPppCpState'
_C='read-only'
_B='current'
_A='TIMETRA-PPP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_i,_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeInterval','TimeStamp')
tmnxChassisIndex,tmnxHwConformance,tmnxHwNotification,tmnxHwObjs=mibBuilder.importSymbols(_j,_k,'tmnxHwConformance','tmnxHwNotification','tmnxHwObjs')
timetraSRMIBModules,=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules')
tmnxPortPortID,=mibBuilder.importSymbols(_l,_m)
TmnxPppCpState,=mibBuilder.importSymbols('TIMETRA-TC-MIB','TmnxPppCpState')
tmnxPppMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,26))
if mibBuilder.loadTexts:tmnxPppMIBModule.setRevisions(('2008-01-01 00:00','2007-01-01 00:00','2006-03-15 00:00','2005-01-24 00:00','2004-03-01 00:00'))
_TmnxPppConformance_ObjectIdentity=ObjectIdentity
tmnxPppConformance=_TmnxPppConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,2,3))
_TmnxPppCompliances_ObjectIdentity=ObjectIdentity
tmnxPppCompliances=_TmnxPppCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,2,3,1))
_TmnxPppGroups_ObjectIdentity=ObjectIdentity
tmnxPppGroups=_TmnxPppGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,2,3,2))
_TmnxPppObjs_ObjectIdentity=ObjectIdentity
tmnxPppObjs=_TmnxPppObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,2,5))
_TmnxPppTable_Object=MibTable
tmnxPppTable=_TmnxPppTable_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1))
if mibBuilder.loadTexts:tmnxPppTable.setStatus(_B)
_TmnxPppEntry_Object=MibTableRow
tmnxPppEntry=_TmnxPppEntry_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1))
tmnxPppEntry.setIndexNames((0,_j,_k),(0,_l,_m))
if mibBuilder.loadTexts:tmnxPppEntry.setStatus(_B)
class _TmnxPppLinkPhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dead',1),('establish',2),('authenticate',3),('network',4),('terminate',5)))
_TmnxPppLinkPhase_Type.__name__=_O
_TmnxPppLinkPhase_Object=MibTableColumn
tmnxPppLinkPhase=_TmnxPppLinkPhase_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,1),_TmnxPppLinkPhase_Type())
tmnxPppLinkPhase.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLinkPhase.setStatus(_B)
_TmnxPppLocalAddress_Type=IpAddress
_TmnxPppLocalAddress_Object=MibTableColumn
tmnxPppLocalAddress=_TmnxPppLocalAddress_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,2),_TmnxPppLocalAddress_Type())
tmnxPppLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalAddress.setStatus(_E)
_TmnxPppRemoteAddress_Type=IpAddress
_TmnxPppRemoteAddress_Object=MibTableColumn
tmnxPppRemoteAddress=_TmnxPppRemoteAddress_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,3),_TmnxPppRemoteAddress_Type())
tmnxPppRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteAddress.setStatus(_E)
_TmnxPppRemoteMacAddress_Type=MacAddress
_TmnxPppRemoteMacAddress_Object=MibTableColumn
tmnxPppRemoteMacAddress=_TmnxPppRemoteMacAddress_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,4),_TmnxPppRemoteMacAddress_Type())
tmnxPppRemoteMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteMacAddress.setStatus(_B)
class _TmnxPppLineMonitorMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('keepalive',2),('lqm',3)))
_TmnxPppLineMonitorMethod_Type.__name__=_O
_TmnxPppLineMonitorMethod_Object=MibTableColumn
tmnxPppLineMonitorMethod=_TmnxPppLineMonitorMethod_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,5),_TmnxPppLineMonitorMethod_Type())
tmnxPppLineMonitorMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLineMonitorMethod.setStatus(_B)
class _TmnxPppKaPeriod_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TmnxPppKaPeriod_Type.__name__=_J
_TmnxPppKaPeriod_Object=MibTableColumn
tmnxPppKaPeriod=_TmnxPppKaPeriod_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,6),_TmnxPppKaPeriod_Type())
tmnxPppKaPeriod.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPppKaPeriod.setStatus(_B)
if mibBuilder.loadTexts:tmnxPppKaPeriod.setUnits(_w)
class _TmnxPppKaDropCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TmnxPppKaDropCount_Type.__name__=_J
_TmnxPppKaDropCount_Object=MibTableColumn
tmnxPppKaDropCount=_TmnxPppKaDropCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,7),_TmnxPppKaDropCount_Type())
tmnxPppKaDropCount.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPppKaDropCount.setStatus(_B)
_TmnxPppKaLastClearedTime_Type=TimeStamp
_TmnxPppKaLastClearedTime_Object=MibTableColumn
tmnxPppKaLastClearedTime=_TmnxPppKaLastClearedTime_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,8),_TmnxPppKaLastClearedTime_Type())
tmnxPppKaLastClearedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppKaLastClearedTime.setStatus(_B)
_TmnxPppKaThresholdExceedsCount_Type=Counter32
_TmnxPppKaThresholdExceedsCount_Object=MibTableColumn
tmnxPppKaThresholdExceedsCount=_TmnxPppKaThresholdExceedsCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,9),_TmnxPppKaThresholdExceedsCount_Type())
tmnxPppKaThresholdExceedsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppKaThresholdExceedsCount.setStatus(_B)
_TmnxPppKaInPktCount_Type=Counter32
_TmnxPppKaInPktCount_Object=MibTableColumn
tmnxPppKaInPktCount=_TmnxPppKaInPktCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,10),_TmnxPppKaInPktCount_Type())
tmnxPppKaInPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppKaInPktCount.setStatus(_B)
_TmnxPppKaOutPktCount_Type=Counter32
_TmnxPppKaOutPktCount_Object=MibTableColumn
tmnxPppKaOutPktCount=_TmnxPppKaOutPktCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,11),_TmnxPppKaOutPktCount_Type())
tmnxPppKaOutPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppKaOutPktCount.setStatus(_B)
_TmnxPppKaTimeDropLink_Type=TimeInterval
_TmnxPppKaTimeDropLink_Object=MibTableColumn
tmnxPppKaTimeDropLink=_TmnxPppKaTimeDropLink_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,12),_TmnxPppKaTimeDropLink_Type())
tmnxPppKaTimeDropLink.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppKaTimeDropLink.setStatus(_B)
class _TmnxPppQuality_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxPppQuality_Type.__name__=_J
_TmnxPppQuality_Object=MibTableColumn
tmnxPppQuality=_TmnxPppQuality_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,13),_TmnxPppQuality_Type())
tmnxPppQuality.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPppQuality.setStatus(_B)
class _TmnxPppLqmOperPeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TmnxPppLqmOperPeriod_Type.__name__=_J
_TmnxPppLqmOperPeriod_Object=MibTableColumn
tmnxPppLqmOperPeriod=_TmnxPppLqmOperPeriod_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,14),_TmnxPppLqmOperPeriod_Type())
tmnxPppLqmOperPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmOperPeriod.setStatus(_B)
if mibBuilder.loadTexts:tmnxPppLqmOperPeriod.setUnits(_w)
class _TmnxPppLqmInRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxPppLqmInRate_Type.__name__=_i
_TmnxPppLqmInRate_Object=MibTableColumn
tmnxPppLqmInRate=_TmnxPppLqmInRate_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,15),_TmnxPppLqmInRate_Type())
tmnxPppLqmInRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmInRate.setStatus(_B)
if mibBuilder.loadTexts:tmnxPppLqmInRate.setUnits(_x)
class _TmnxPppLqmOutRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TmnxPppLqmOutRate_Type.__name__=_i
_TmnxPppLqmOutRate_Object=MibTableColumn
tmnxPppLqmOutRate=_TmnxPppLqmOutRate_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,16),_TmnxPppLqmOutRate_Type())
tmnxPppLqmOutRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmOutRate.setStatus(_B)
if mibBuilder.loadTexts:tmnxPppLqmOutRate.setUnits(_x)
_TmnxPppLqmLastClearedTime_Type=TimeStamp
_TmnxPppLqmLastClearedTime_Object=MibTableColumn
tmnxPppLqmLastClearedTime=_TmnxPppLqmLastClearedTime_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,17),_TmnxPppLqmLastClearedTime_Type())
tmnxPppLqmLastClearedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmLastClearedTime.setStatus(_B)
_TmnxPppLqmThresholdExceedsCount_Type=Counter32
_TmnxPppLqmThresholdExceedsCount_Object=MibTableColumn
tmnxPppLqmThresholdExceedsCount=_TmnxPppLqmThresholdExceedsCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,18),_TmnxPppLqmThresholdExceedsCount_Type())
tmnxPppLqmThresholdExceedsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmThresholdExceedsCount.setStatus(_B)
_TmnxPppLqmInPktCount_Type=Counter32
_TmnxPppLqmInPktCount_Object=MibTableColumn
tmnxPppLqmInPktCount=_TmnxPppLqmInPktCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,19),_TmnxPppLqmInPktCount_Type())
tmnxPppLqmInPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmInPktCount.setStatus(_B)
_TmnxPppLqmOutPktCount_Type=Counter32
_TmnxPppLqmOutPktCount_Object=MibTableColumn
tmnxPppLqmOutPktCount=_TmnxPppLqmOutPktCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,20),_TmnxPppLqmOutPktCount_Type())
tmnxPppLqmOutPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmOutPktCount.setStatus(_B)
_TmnxPppLqmTimeDropLink_Type=TimeInterval
_TmnxPppLqmTimeDropLink_Object=MibTableColumn
tmnxPppLqmTimeDropLink=_TmnxPppLqmTimeDropLink_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,21),_TmnxPppLqmTimeDropLink_Type())
tmnxPppLqmTimeDropLink.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLqmTimeDropLink.setStatus(_B)
_TmnxPppLocalMagicNumber_Type=Unsigned32
_TmnxPppLocalMagicNumber_Object=MibTableColumn
tmnxPppLocalMagicNumber=_TmnxPppLocalMagicNumber_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,22),_TmnxPppLocalMagicNumber_Type())
tmnxPppLocalMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalMagicNumber.setStatus(_B)
_TmnxPppRemoteMagicNumber_Type=Unsigned32
_TmnxPppRemoteMagicNumber_Object=MibTableColumn
tmnxPppRemoteMagicNumber=_TmnxPppRemoteMagicNumber_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,23),_TmnxPppRemoteMagicNumber_Type())
tmnxPppRemoteMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteMagicNumber.setStatus(_B)
_TmnxPppLocalIPv4AddressType_Type=InetAddressType
_TmnxPppLocalIPv4AddressType_Object=MibTableColumn
tmnxPppLocalIPv4AddressType=_TmnxPppLocalIPv4AddressType_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,24),_TmnxPppLocalIPv4AddressType_Type())
tmnxPppLocalIPv4AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalIPv4AddressType.setStatus(_B)
class _TmnxPppLocalIPv4Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TmnxPppLocalIPv4Address_Type.__name__=_I
_TmnxPppLocalIPv4Address_Object=MibTableColumn
tmnxPppLocalIPv4Address=_TmnxPppLocalIPv4Address_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,25),_TmnxPppLocalIPv4Address_Type())
tmnxPppLocalIPv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalIPv4Address.setStatus(_B)
_TmnxPppLocalIPv6AddressType_Type=InetAddressType
_TmnxPppLocalIPv6AddressType_Object=MibTableColumn
tmnxPppLocalIPv6AddressType=_TmnxPppLocalIPv6AddressType_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,26),_TmnxPppLocalIPv6AddressType_Type())
tmnxPppLocalIPv6AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalIPv6AddressType.setStatus(_B)
class _TmnxPppLocalIPv6Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_TmnxPppLocalIPv6Address_Type.__name__=_I
_TmnxPppLocalIPv6Address_Object=MibTableColumn
tmnxPppLocalIPv6Address=_TmnxPppLocalIPv6Address_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,27),_TmnxPppLocalIPv6Address_Type())
tmnxPppLocalIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppLocalIPv6Address.setStatus(_B)
_TmnxPppRemoteIPv4AddressType_Type=InetAddressType
_TmnxPppRemoteIPv4AddressType_Object=MibTableColumn
tmnxPppRemoteIPv4AddressType=_TmnxPppRemoteIPv4AddressType_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,28),_TmnxPppRemoteIPv4AddressType_Type())
tmnxPppRemoteIPv4AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteIPv4AddressType.setStatus(_B)
class _TmnxPppRemoteIPv4Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TmnxPppRemoteIPv4Address_Type.__name__=_I
_TmnxPppRemoteIPv4Address_Object=MibTableColumn
tmnxPppRemoteIPv4Address=_TmnxPppRemoteIPv4Address_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,29),_TmnxPppRemoteIPv4Address_Type())
tmnxPppRemoteIPv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteIPv4Address.setStatus(_B)
_TmnxPppRemoteIPv6AddressType_Type=InetAddressType
_TmnxPppRemoteIPv6AddressType_Object=MibTableColumn
tmnxPppRemoteIPv6AddressType=_TmnxPppRemoteIPv6AddressType_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,30),_TmnxPppRemoteIPv6AddressType_Type())
tmnxPppRemoteIPv6AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteIPv6AddressType.setStatus(_B)
class _TmnxPppRemoteIPv6Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_TmnxPppRemoteIPv6Address_Type.__name__=_I
_TmnxPppRemoteIPv6Address_Object=MibTableColumn
tmnxPppRemoteIPv6Address=_TmnxPppRemoteIPv6Address_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,31),_TmnxPppRemoteIPv6Address_Type())
tmnxPppRemoteIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppRemoteIPv6Address.setStatus(_B)
class _TmnxPppHdrCompression_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('acfc',0),('pfc',1)))
_TmnxPppHdrCompression_Type.__name__='Bits'
_TmnxPppHdrCompression_Object=MibTableColumn
tmnxPppHdrCompression=_TmnxPppHdrCompression_Object((1,3,6,1,4,1,6527,3,1,2,2,5,1,1,32),_TmnxPppHdrCompression_Type())
tmnxPppHdrCompression.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPppHdrCompression.setStatus(_B)
_TmnxPppCpTable_Object=MibTable
tmnxPppCpTable=_TmnxPppCpTable_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2))
if mibBuilder.loadTexts:tmnxPppCpTable.setStatus(_B)
_TmnxPppCpEntry_Object=MibTableRow
tmnxPppCpEntry=_TmnxPppCpEntry_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1))
tmnxPppCpEntry.setIndexNames((0,_j,_k),(0,_l,_m),(0,_A,_y))
if mibBuilder.loadTexts:tmnxPppCpEntry.setStatus(_B)
class _TmnxPppCpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('lcp',1),('ipcp',2),('mplscp',3),('bcp',4),('osicp',5),('lqr',6),('ipv6cp',7)))
_TmnxPppCpProtocol_Type.__name__=_O
_TmnxPppCpProtocol_Object=MibTableColumn
tmnxPppCpProtocol=_TmnxPppCpProtocol_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1,1),_TmnxPppCpProtocol_Type())
tmnxPppCpProtocol.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxPppCpProtocol.setStatus(_B)
_TmnxPppCpState_Type=TmnxPppCpState
_TmnxPppCpState_Object=MibTableColumn
tmnxPppCpState=_TmnxPppCpState_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1,2),_TmnxPppCpState_Type())
tmnxPppCpState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppCpState.setStatus(_B)
_TmnxPppCpLastChange_Type=TimeStamp
_TmnxPppCpLastChange_Object=MibTableColumn
tmnxPppCpLastChange=_TmnxPppCpLastChange_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1,3),_TmnxPppCpLastChange_Type())
tmnxPppCpLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppCpLastChange.setStatus(_B)
_TmnxPppCpRestartCount_Type=Counter32
_TmnxPppCpRestartCount_Object=MibTableColumn
tmnxPppCpRestartCount=_TmnxPppCpRestartCount_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1,4),_TmnxPppCpRestartCount_Type())
tmnxPppCpRestartCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppCpRestartCount.setStatus(_B)
_TmnxPppCpLastClearedTime_Type=TimeStamp
_TmnxPppCpLastClearedTime_Object=MibTableColumn
tmnxPppCpLastClearedTime=_TmnxPppCpLastClearedTime_Object((1,3,6,1,4,1,6527,3,1,2,2,5,2,1,5),_TmnxPppCpLastClearedTime_Type())
tmnxPppCpLastClearedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPppCpLastClearedTime.setStatus(_B)
_TmnxPppNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxPppNotifyPrefix=_TmnxPppNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,2,3))
_TmnxPppNotification_ObjectIdentity=ObjectIdentity
tmnxPppNotification=_TmnxPppNotification_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,2,3,0))
tmnxPppGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,1))
tmnxPppGroup.setObjects(*((_A,_Q),(_A,_n),(_A,_o),(_A,_R),(_A,_S),(_A,_K),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_F),(_A,_G),(_A,_D),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:tmnxPppGroup.setStatus(_E)
tmnxPPPObsoleteV4v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,4))
tmnxPPPObsoleteV4v0Group.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:tmnxPPPObsoleteV4v0Group.setStatus(_B)
tmnxPpp7450V4v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,5))
tmnxPpp7450V4v0Group.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_K),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_F),(_A,_G),(_A,_D),(_A,_f),(_A,_g),(_A,_h),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:tmnxPpp7450V4v0Group.setStatus(_B)
tmnxPpp7750V4v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,6))
tmnxPpp7750V4v0Group.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_K),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_F),(_A,_G),(_A,_D),(_A,_f),(_A,_g),(_A,_h),(_A,_p),(_A,_q),(_A,_z),(_A,_A0),(_A,_r),(_A,_s),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:tmnxPpp7750V4v0Group.setStatus(_B)
tmnxPppCompressionGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,7))
tmnxPppCompressionGroup.setObjects((_A,_A3))
if mibBuilder.loadTexts:tmnxPppCompressionGroup.setStatus(_B)
tmnxPppCpUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,1))
tmnxPppCpUp.setObjects((_A,_D))
if mibBuilder.loadTexts:tmnxPppCpUp.setStatus(_B)
tmnxPppCpDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,2))
tmnxPppCpDown.setObjects((_A,_D))
if mibBuilder.loadTexts:tmnxPppCpDown.setStatus(_B)
tmnxPppNcpUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,3))
tmnxPppNcpUp.setObjects((_A,_D))
if mibBuilder.loadTexts:tmnxPppNcpUp.setStatus(_B)
tmnxPppNcpDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,4))
tmnxPppNcpDown.setObjects((_A,_D))
if mibBuilder.loadTexts:tmnxPppNcpDown.setStatus(_B)
tmnxPppKeepaliveFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,5))
tmnxPppKeepaliveFailure.setObjects((_A,_K))
if mibBuilder.loadTexts:tmnxPppKeepaliveFailure.setStatus(_B)
tmnxPppLqmFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,6))
tmnxPppLqmFailure.setObjects(*((_A,_M),(_A,_N),(_A,_L)))
if mibBuilder.loadTexts:tmnxPppLqmFailure.setStatus(_B)
tmnxPppLoopback=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,7))
tmnxPppLoopback.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:tmnxPppLoopback.setStatus(_B)
tmnxPppLoopbackClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,2,3,0,8))
tmnxPppLoopbackClear.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:tmnxPppLoopbackClear.setStatus(_B)
tmnxPppNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,2,3,2,3))
tmnxPppNotificationGroup.setObjects(*((_A,_A4),(_A,_t),(_A,_t),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:tmnxPppNotificationGroup.setStatus(_B)
tmnxPppCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,2,3,1,1))
tmnxPppCompliance.setObjects(*((_A,_AB),(_A,_H)))
if mibBuilder.loadTexts:tmnxPppCompliance.setStatus(_E)
tmnxPpp7450V4v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,2,3,1,2))
tmnxPpp7450V4v0Compliance.setObjects(*((_A,_u),(_A,_H)))
if mibBuilder.loadTexts:tmnxPpp7450V4v0Compliance.setStatus(_E)
tmnxPpp7750V4v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,2,3,1,3))
tmnxPpp7750V4v0Compliance.setObjects(*((_A,_v),(_A,_H)))
if mibBuilder.loadTexts:tmnxPpp7750V4v0Compliance.setStatus(_E)
tmnxPpp7450V6v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,2,3,1,4))
tmnxPpp7450V6v0Compliance.setObjects(*((_A,_u),(_A,_H)))
if mibBuilder.loadTexts:tmnxPpp7450V6v0Compliance.setStatus(_B)
tmnxPpp77x0V6v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,2,3,1,5))
tmnxPpp77x0V6v0Compliance.setObjects(*((_A,_v),(_A,_H),(_A,_AC)))
if mibBuilder.loadTexts:tmnxPpp77x0V6v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'tmnxPppMIBModule':tmnxPppMIBModule,'tmnxPppConformance':tmnxPppConformance,'tmnxPppCompliances':tmnxPppCompliances,'tmnxPppCompliance':tmnxPppCompliance,'tmnxPpp7450V4v0Compliance':tmnxPpp7450V4v0Compliance,'tmnxPpp7750V4v0Compliance':tmnxPpp7750V4v0Compliance,'tmnxPpp7450V6v0Compliance':tmnxPpp7450V6v0Compliance,'tmnxPpp77x0V6v0Compliance':tmnxPpp77x0V6v0Compliance,'tmnxPppGroups':tmnxPppGroups,_AB:tmnxPppGroup,_H:tmnxPppNotificationGroup,'tmnxPPPObsoleteV4v0Group':tmnxPPPObsoleteV4v0Group,_u:tmnxPpp7450V4v0Group,_v:tmnxPpp7750V4v0Group,_AC:tmnxPppCompressionGroup,'tmnxPppObjs':tmnxPppObjs,'tmnxPppTable':tmnxPppTable,'tmnxPppEntry':tmnxPppEntry,_Q:tmnxPppLinkPhase,_n:tmnxPppLocalAddress,_o:tmnxPppRemoteAddress,_R:tmnxPppRemoteMacAddress,_S:tmnxPppLineMonitorMethod,_K:tmnxPppKaPeriod,_T:tmnxPppKaDropCount,_U:tmnxPppKaLastClearedTime,_V:tmnxPppKaThresholdExceedsCount,_W:tmnxPppKaInPktCount,_X:tmnxPppKaOutPktCount,_Y:tmnxPppKaTimeDropLink,_L:tmnxPppQuality,_Z:tmnxPppLqmOperPeriod,_M:tmnxPppLqmInRate,_N:tmnxPppLqmOutRate,_a:tmnxPppLqmLastClearedTime,_b:tmnxPppLqmThresholdExceedsCount,_c:tmnxPppLqmInPktCount,_d:tmnxPppLqmOutPktCount,_e:tmnxPppLqmTimeDropLink,_F:tmnxPppLocalMagicNumber,_G:tmnxPppRemoteMagicNumber,_p:tmnxPppLocalIPv4AddressType,_q:tmnxPppLocalIPv4Address,_z:tmnxPppLocalIPv6AddressType,_A0:tmnxPppLocalIPv6Address,_r:tmnxPppRemoteIPv4AddressType,_s:tmnxPppRemoteIPv4Address,_A1:tmnxPppRemoteIPv6AddressType,_A2:tmnxPppRemoteIPv6Address,_A3:tmnxPppHdrCompression,'tmnxPppCpTable':tmnxPppCpTable,'tmnxPppCpEntry':tmnxPppCpEntry,_y:tmnxPppCpProtocol,_D:tmnxPppCpState,_f:tmnxPppCpLastChange,_g:tmnxPppCpRestartCount,_h:tmnxPppCpLastClearedTime,'tmnxPppNotifyPrefix':tmnxPppNotifyPrefix,'tmnxPppNotification':tmnxPppNotification,_A4:tmnxPppCpUp,_t:tmnxPppCpDown,_A5:tmnxPppNcpUp,_A6:tmnxPppNcpDown,_A7:tmnxPppKeepaliveFailure,_A8:tmnxPppLqmFailure,_A9:tmnxPppLoopback,_AA:tmnxPppLoopbackClear})