_N='eltLtcTunnelShutdownThreshold'
_M='eltLtcTunnelDropThreshold'
_L='eltLtcTunneledProtocolIndex'
_K='PDUs/sec'
_J='not-accessible'
_I='eltLtcTunnelThresholdProtocolIndex'
_H='MacAddress'
_G='read-only'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='ELTEX-MES-L2-TUNNEL-CONFIG-MIB'
_B='read-write'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QosLayer2Cos,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','QosLayer2Cos')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_H,'PhysAddress','TextualConvention','TruthValue')
eltMesL2TunnelConfig=ModuleIdentity((1,3,6,1,4,1,35265,1,23,13))
if mibBuilder.loadTexts:eltMesL2TunnelConfig.setRevisions(('2015-11-19 00:00',))
class EltLtcTunneledProtocolIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('stp',1))
_EltMesLtcMIBObjects_ObjectIdentity=ObjectIdentity
eltMesLtcMIBObjects=_EltMesLtcMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,1))
_EltMesLtcGlobal_ObjectIdentity=ObjectIdentity
eltMesLtcGlobal=_EltMesLtcGlobal_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,1,1))
_EltLtcNotificationEnable_Type=TruthValue
_EltLtcNotificationEnable_Object=MibScalar
eltLtcNotificationEnable=_EltLtcNotificationEnable_Object((1,3,6,1,4,1,35265,1,23,13,1,1,1),_EltLtcNotificationEnable_Type())
eltLtcNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcNotificationEnable.setStatus(_A)
class _EltLtcTunnelMacAddress_Type(MacAddress):defaultHexValue='0100EEEE0000'
_EltLtcTunnelMacAddress_Type.__name__=_H
_EltLtcTunnelMacAddress_Object=MibScalar
eltLtcTunnelMacAddress=_EltLtcTunnelMacAddress_Object((1,3,6,1,4,1,35265,1,23,13,1,1,2),_EltLtcTunnelMacAddress_Type())
eltLtcTunnelMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcTunnelMacAddress.setStatus(_A)
_EltMesLtcTunneledProtocol_ObjectIdentity=ObjectIdentity
eltMesLtcTunneledProtocol=_EltMesLtcTunneledProtocol_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,1,2))
_EltLtcTunneledProtocolTable_Object=MibTable
eltLtcTunneledProtocolTable=_EltLtcTunneledProtocolTable_Object((1,3,6,1,4,1,35265,1,23,13,1,2,1))
if mibBuilder.loadTexts:eltLtcTunneledProtocolTable.setStatus(_A)
_EltLtcTunneledProtocolEntry_Object=MibTableRow
eltLtcTunneledProtocolEntry=_EltLtcTunneledProtocolEntry_Object((1,3,6,1,4,1,35265,1,23,13,1,2,1,1))
eltLtcTunneledProtocolEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltLtcTunneledProtocolEntry.setStatus(_A)
class _EltLtcTunneledProtocolType_Type(Bits):namedValues=NamedValues(*(('stp',0),('workaround',1)))
_EltLtcTunneledProtocolType_Type.__name__='Bits'
_EltLtcTunneledProtocolType_Object=MibTableColumn
eltLtcTunneledProtocolType=_EltLtcTunneledProtocolType_Object((1,3,6,1,4,1,35265,1,23,13,1,2,1,1,1),_EltLtcTunneledProtocolType_Type())
eltLtcTunneledProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcTunneledProtocolType.setStatus(_A)
_EltLtcTunnelCos_Type=QosLayer2Cos
_EltLtcTunnelCos_Object=MibTableColumn
eltLtcTunnelCos=_EltLtcTunnelCos_Object((1,3,6,1,4,1,35265,1,23,13,1,2,1,1,2),_EltLtcTunnelCos_Type())
eltLtcTunnelCos.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcTunnelCos.setStatus(_A)
_EltMesLtcTunnelThreshold_ObjectIdentity=ObjectIdentity
eltMesLtcTunnelThreshold=_EltMesLtcTunnelThreshold_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,1,3))
_EltLtcTunnelThresholdTable_Object=MibTable
eltLtcTunnelThresholdTable=_EltLtcTunnelThresholdTable_Object((1,3,6,1,4,1,35265,1,23,13,1,3,1))
if mibBuilder.loadTexts:eltLtcTunnelThresholdTable.setStatus(_A)
_EltLtcTunnelThresholdEntry_Object=MibTableRow
eltLtcTunnelThresholdEntry=_EltLtcTunnelThresholdEntry_Object((1,3,6,1,4,1,35265,1,23,13,1,3,1,1))
eltLtcTunnelThresholdEntry.setIndexNames((0,_D,_E),(0,_C,_I))
if mibBuilder.loadTexts:eltLtcTunnelThresholdEntry.setStatus(_A)
_EltLtcTunnelThresholdProtocolIndex_Type=EltLtcTunneledProtocolIndex
_EltLtcTunnelThresholdProtocolIndex_Object=MibTableColumn
eltLtcTunnelThresholdProtocolIndex=_EltLtcTunnelThresholdProtocolIndex_Object((1,3,6,1,4,1,35265,1,23,13,1,3,1,1,1),_EltLtcTunnelThresholdProtocolIndex_Type())
eltLtcTunnelThresholdProtocolIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eltLtcTunnelThresholdProtocolIndex.setStatus(_A)
class _EltLtcTunnelDropThreshold_Type(Unsigned32):defaultValue=0
_EltLtcTunnelDropThreshold_Type.__name__=_F
_EltLtcTunnelDropThreshold_Object=MibTableColumn
eltLtcTunnelDropThreshold=_EltLtcTunnelDropThreshold_Object((1,3,6,1,4,1,35265,1,23,13,1,3,1,1,2),_EltLtcTunnelDropThreshold_Type())
eltLtcTunnelDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcTunnelDropThreshold.setStatus(_A)
if mibBuilder.loadTexts:eltLtcTunnelDropThreshold.setUnits(_K)
class _EltLtcTunnelShutdownThreshold_Type(Unsigned32):defaultValue=0
_EltLtcTunnelShutdownThreshold_Type.__name__=_F
_EltLtcTunnelShutdownThreshold_Object=MibTableColumn
eltLtcTunnelShutdownThreshold=_EltLtcTunnelShutdownThreshold_Object((1,3,6,1,4,1,35265,1,23,13,1,3,1,1,3),_EltLtcTunnelShutdownThreshold_Type())
eltLtcTunnelShutdownThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLtcTunnelShutdownThreshold.setStatus(_A)
if mibBuilder.loadTexts:eltLtcTunnelShutdownThreshold.setUnits(_K)
_EltMesLtcTunnelStatistics_ObjectIdentity=ObjectIdentity
eltMesLtcTunnelStatistics=_EltMesLtcTunnelStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,1,4))
_EltLtcTunnelStatisticsTable_Object=MibTable
eltLtcTunnelStatisticsTable=_EltLtcTunnelStatisticsTable_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1))
if mibBuilder.loadTexts:eltLtcTunnelStatisticsTable.setStatus(_A)
_EltLtcTunnelStatisticsEntry_Object=MibTableRow
eltLtcTunnelStatisticsEntry=_EltLtcTunnelStatisticsEntry_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1,1))
eltLtcTunnelStatisticsEntry.setIndexNames((0,_D,_E),(0,_C,_L))
if mibBuilder.loadTexts:eltLtcTunnelStatisticsEntry.setStatus(_A)
_EltLtcTunneledProtocolIndex_Type=EltLtcTunneledProtocolIndex
_EltLtcTunneledProtocolIndex_Object=MibTableColumn
eltLtcTunneledProtocolIndex=_EltLtcTunneledProtocolIndex_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1,1,1),_EltLtcTunneledProtocolIndex_Type())
eltLtcTunneledProtocolIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eltLtcTunneledProtocolIndex.setStatus(_A)
_EltLtcTunnelEncapStats_Type=Counter32
_EltLtcTunnelEncapStats_Object=MibTableColumn
eltLtcTunnelEncapStats=_EltLtcTunnelEncapStats_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1,1,2),_EltLtcTunnelEncapStats_Type())
eltLtcTunnelEncapStats.setMaxAccess(_G)
if mibBuilder.loadTexts:eltLtcTunnelEncapStats.setStatus(_A)
if mibBuilder.loadTexts:eltLtcTunnelEncapStats.setUnits('encapsulated PDUs')
_EltLtcTunnelDecapStats_Type=Counter32
_EltLtcTunnelDecapStats_Object=MibTableColumn
eltLtcTunnelDecapStats=_EltLtcTunnelDecapStats_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1,1,3),_EltLtcTunnelDecapStats_Type())
eltLtcTunnelDecapStats.setMaxAccess(_G)
if mibBuilder.loadTexts:eltLtcTunnelDecapStats.setStatus(_A)
if mibBuilder.loadTexts:eltLtcTunnelDecapStats.setUnits('de-encapsulated PDUs')
_EltLtcTunnelDropStats_Type=Counter32
_EltLtcTunnelDropStats_Object=MibTableColumn
eltLtcTunnelDropStats=_EltLtcTunnelDropStats_Object((1,3,6,1,4,1,35265,1,23,13,1,4,1,1,4),_EltLtcTunnelDropStats_Type())
eltLtcTunnelDropStats.setMaxAccess(_G)
if mibBuilder.loadTexts:eltLtcTunnelDropStats.setStatus(_A)
if mibBuilder.loadTexts:eltLtcTunnelDropStats.setUnits('PDUs')
_EltMesLtcMIBNotifications_ObjectIdentity=ObjectIdentity
eltMesLtcMIBNotifications=_EltMesLtcMIBNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,2))
_EltMesLtcMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesLtcMIBNotificationsPrefix=_EltMesLtcMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,23,13,2,0))
eltLtcTunnelDropThresholdExceeded=NotificationType((1,3,6,1,4,1,35265,1,23,13,2,0,1))
eltLtcTunnelDropThresholdExceeded.setObjects((_C,_M))
if mibBuilder.loadTexts:eltLtcTunnelDropThresholdExceeded.setStatus(_A)
eltLtcTunnelShutdownThresholdExceeded=NotificationType((1,3,6,1,4,1,35265,1,23,13,2,0,2))
eltLtcTunnelShutdownThresholdExceeded.setObjects((_C,_N))
if mibBuilder.loadTexts:eltLtcTunnelShutdownThresholdExceeded.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EltLtcTunneledProtocolIndex':EltLtcTunneledProtocolIndex,'eltMesL2TunnelConfig':eltMesL2TunnelConfig,'eltMesLtcMIBObjects':eltMesLtcMIBObjects,'eltMesLtcGlobal':eltMesLtcGlobal,'eltLtcNotificationEnable':eltLtcNotificationEnable,'eltLtcTunnelMacAddress':eltLtcTunnelMacAddress,'eltMesLtcTunneledProtocol':eltMesLtcTunneledProtocol,'eltLtcTunneledProtocolTable':eltLtcTunneledProtocolTable,'eltLtcTunneledProtocolEntry':eltLtcTunneledProtocolEntry,'eltLtcTunneledProtocolType':eltLtcTunneledProtocolType,'eltLtcTunnelCos':eltLtcTunnelCos,'eltMesLtcTunnelThreshold':eltMesLtcTunnelThreshold,'eltLtcTunnelThresholdTable':eltLtcTunnelThresholdTable,'eltLtcTunnelThresholdEntry':eltLtcTunnelThresholdEntry,_I:eltLtcTunnelThresholdProtocolIndex,_M:eltLtcTunnelDropThreshold,_N:eltLtcTunnelShutdownThreshold,'eltMesLtcTunnelStatistics':eltMesLtcTunnelStatistics,'eltLtcTunnelStatisticsTable':eltLtcTunnelStatisticsTable,'eltLtcTunnelStatisticsEntry':eltLtcTunnelStatisticsEntry,_L:eltLtcTunneledProtocolIndex,'eltLtcTunnelEncapStats':eltLtcTunnelEncapStats,'eltLtcTunnelDecapStats':eltLtcTunnelDecapStats,'eltLtcTunnelDropStats':eltLtcTunnelDropStats,'eltMesLtcMIBNotifications':eltMesLtcMIBNotifications,'eltMesLtcMIBNotificationsPrefix':eltMesLtcMIBNotificationsPrefix,'eltLtcTunnelDropThresholdExceeded':eltLtcTunnelDropThresholdExceeded,'eltLtcTunnelShutdownThresholdExceeded':eltLtcTunnelShutdownThresholdExceeded})