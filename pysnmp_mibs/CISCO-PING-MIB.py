_c='ciscoPingMIBGroupVpn'
_b='ciscoPingMIBGroup'
_a='ciscoPingCompletion'
_Z='ciscoPingVrfName'
_Y='obsolete'
_X='ciscoPingSerialNumber'
_W='TruthValue'
_V='OctetString'
_U='ciscoPingEntryStatus'
_T='ciscoPingEntryOwner'
_S='ciscoPingMaxRtt'
_R='ciscoPingAvgRtt'
_Q='ciscoPingMinRtt'
_P='ciscoPingTrapOnCompletion'
_O='ciscoPingDelay'
_N='ciscoPingPacketTimeout'
_M='ciscoPingPacketSize'
_L='ciscoPingPacketCount'
_K='ciscoPingAddress'
_J='ciscoPingProtocol'
_I='ciscoPingCompleted'
_H='ciscoPingReceivedPackets'
_G='ciscoPingSentPackets'
_F='milliseconds'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='current'
_A='CISCO-PING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoNetworkAddress,CiscoNetworkProtocol=mibBuilder.importSymbols('CISCO-TC','CiscoNetworkAddress','CiscoNetworkProtocol')
OwnerString,=mibBuilder.importSymbols('IF-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_W)
ciscoPingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,16))
if mibBuilder.loadTexts:ciscoPingMIB.setRevisions(('2001-08-28 00:00','2001-05-14 00:00','1999-10-08 00:00','1994-11-11 00:00','1994-07-22 00:00'))
_CiscoPingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPingMIBObjects=_CiscoPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,16,1))
_CiscoPingTable_Object=MibTable
ciscoPingTable=_CiscoPingTable_Object((1,3,6,1,4,1,9,9,16,1,1))
if mibBuilder.loadTexts:ciscoPingTable.setStatus(_B)
_CiscoPingEntry_Object=MibTableRow
ciscoPingEntry=_CiscoPingEntry_Object((1,3,6,1,4,1,9,9,16,1,1,1))
ciscoPingEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:ciscoPingEntry.setStatus(_B)
class _CiscoPingSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoPingSerialNumber_Type.__name__=_D
_CiscoPingSerialNumber_Object=MibTableColumn
ciscoPingSerialNumber=_CiscoPingSerialNumber_Object((1,3,6,1,4,1,9,9,16,1,1,1,1),_CiscoPingSerialNumber_Type())
ciscoPingSerialNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoPingSerialNumber.setStatus(_B)
_CiscoPingProtocol_Type=CiscoNetworkProtocol
_CiscoPingProtocol_Object=MibTableColumn
ciscoPingProtocol=_CiscoPingProtocol_Object((1,3,6,1,4,1,9,9,16,1,1,1,2),_CiscoPingProtocol_Type())
ciscoPingProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingProtocol.setStatus(_B)
_CiscoPingAddress_Type=CiscoNetworkAddress
_CiscoPingAddress_Object=MibTableColumn
ciscoPingAddress=_CiscoPingAddress_Object((1,3,6,1,4,1,9,9,16,1,1,1,3),_CiscoPingAddress_Type())
ciscoPingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingAddress.setStatus(_B)
class _CiscoPingPacketCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoPingPacketCount_Type.__name__=_D
_CiscoPingPacketCount_Object=MibTableColumn
ciscoPingPacketCount=_CiscoPingPacketCount_Object((1,3,6,1,4,1,9,9,16,1,1,1,4),_CiscoPingPacketCount_Type())
ciscoPingPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingPacketCount.setStatus(_B)
class _CiscoPingPacketSize_Type(Integer32):defaultValue=100
_CiscoPingPacketSize_Type.__name__=_D
_CiscoPingPacketSize_Object=MibTableColumn
ciscoPingPacketSize=_CiscoPingPacketSize_Object((1,3,6,1,4,1,9,9,16,1,1,1,5),_CiscoPingPacketSize_Type())
ciscoPingPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingPacketSize.setStatus(_B)
class _CiscoPingPacketTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_CiscoPingPacketTimeout_Type.__name__=_D
_CiscoPingPacketTimeout_Object=MibTableColumn
ciscoPingPacketTimeout=_CiscoPingPacketTimeout_Object((1,3,6,1,4,1,9,9,16,1,1,1,6),_CiscoPingPacketTimeout_Type())
ciscoPingPacketTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingPacketTimeout.setStatus(_B)
if mibBuilder.loadTexts:ciscoPingPacketTimeout.setUnits(_F)
class _CiscoPingDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_CiscoPingDelay_Type.__name__=_D
_CiscoPingDelay_Object=MibTableColumn
ciscoPingDelay=_CiscoPingDelay_Object((1,3,6,1,4,1,9,9,16,1,1,1,7),_CiscoPingDelay_Type())
ciscoPingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingDelay.setStatus(_B)
if mibBuilder.loadTexts:ciscoPingDelay.setUnits(_F)
class _CiscoPingTrapOnCompletion_Type(TruthValue):defaultValue=2
_CiscoPingTrapOnCompletion_Type.__name__=_W
_CiscoPingTrapOnCompletion_Object=MibTableColumn
ciscoPingTrapOnCompletion=_CiscoPingTrapOnCompletion_Object((1,3,6,1,4,1,9,9,16,1,1,1,8),_CiscoPingTrapOnCompletion_Type())
ciscoPingTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingTrapOnCompletion.setStatus(_B)
_CiscoPingSentPackets_Type=Counter32
_CiscoPingSentPackets_Object=MibTableColumn
ciscoPingSentPackets=_CiscoPingSentPackets_Object((1,3,6,1,4,1,9,9,16,1,1,1,9),_CiscoPingSentPackets_Type())
ciscoPingSentPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingSentPackets.setStatus(_B)
_CiscoPingReceivedPackets_Type=Counter32
_CiscoPingReceivedPackets_Object=MibTableColumn
ciscoPingReceivedPackets=_CiscoPingReceivedPackets_Object((1,3,6,1,4,1,9,9,16,1,1,1,10),_CiscoPingReceivedPackets_Type())
ciscoPingReceivedPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingReceivedPackets.setStatus(_B)
_CiscoPingMinRtt_Type=Integer32
_CiscoPingMinRtt_Object=MibTableColumn
ciscoPingMinRtt=_CiscoPingMinRtt_Object((1,3,6,1,4,1,9,9,16,1,1,1,11),_CiscoPingMinRtt_Type())
ciscoPingMinRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingMinRtt.setStatus(_B)
if mibBuilder.loadTexts:ciscoPingMinRtt.setUnits(_F)
_CiscoPingAvgRtt_Type=Integer32
_CiscoPingAvgRtt_Object=MibTableColumn
ciscoPingAvgRtt=_CiscoPingAvgRtt_Object((1,3,6,1,4,1,9,9,16,1,1,1,12),_CiscoPingAvgRtt_Type())
ciscoPingAvgRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingAvgRtt.setStatus(_B)
if mibBuilder.loadTexts:ciscoPingAvgRtt.setUnits(_F)
_CiscoPingMaxRtt_Type=Integer32
_CiscoPingMaxRtt_Object=MibTableColumn
ciscoPingMaxRtt=_CiscoPingMaxRtt_Object((1,3,6,1,4,1,9,9,16,1,1,1,13),_CiscoPingMaxRtt_Type())
ciscoPingMaxRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingMaxRtt.setStatus(_B)
if mibBuilder.loadTexts:ciscoPingMaxRtt.setUnits(_F)
_CiscoPingCompleted_Type=TruthValue
_CiscoPingCompleted_Object=MibTableColumn
ciscoPingCompleted=_CiscoPingCompleted_Object((1,3,6,1,4,1,9,9,16,1,1,1,14),_CiscoPingCompleted_Type())
ciscoPingCompleted.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoPingCompleted.setStatus(_B)
_CiscoPingEntryOwner_Type=OwnerString
_CiscoPingEntryOwner_Object=MibTableColumn
ciscoPingEntryOwner=_CiscoPingEntryOwner_Object((1,3,6,1,4,1,9,9,16,1,1,1,15),_CiscoPingEntryOwner_Type())
ciscoPingEntryOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingEntryOwner.setStatus(_B)
_CiscoPingEntryStatus_Type=RowStatus
_CiscoPingEntryStatus_Object=MibTableColumn
ciscoPingEntryStatus=_CiscoPingEntryStatus_Object((1,3,6,1,4,1,9,9,16,1,1,1,16),_CiscoPingEntryStatus_Type())
ciscoPingEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingEntryStatus.setStatus(_B)
class _CiscoPingVrfName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoPingVrfName_Type.__name__=_V
_CiscoPingVrfName_Object=MibTableColumn
ciscoPingVrfName=_CiscoPingVrfName_Object((1,3,6,1,4,1,9,9,16,1,1,1,17),_CiscoPingVrfName_Type())
ciscoPingVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPingVrfName.setStatus(_B)
_CiscoPingMIBTrapPrefix_ObjectIdentity=ObjectIdentity
ciscoPingMIBTrapPrefix=_CiscoPingMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,16,2))
_CiscoPingMIBTraps_ObjectIdentity=ObjectIdentity
ciscoPingMIBTraps=_CiscoPingMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,16,2,0))
_CiscoPingMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPingMIBConformance=_CiscoPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,16,3))
_CiscoPingMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPingMIBCompliances=_CiscoPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,16,3,1))
_CiscoPingMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPingMIBGroups=_CiscoPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,16,3,2))
ciscoPingMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,16,3,2,1))
ciscoPingMIBGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_G),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_I),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoPingMIBGroup.setStatus(_Y)
ciscoPingMIBGroupVpn=ObjectGroup((1,3,6,1,4,1,9,9,16,3,2,2))
ciscoPingMIBGroupVpn.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_G),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_I),(_A,_T),(_A,_U),(_A,_Z)))
if mibBuilder.loadTexts:ciscoPingMIBGroupVpn.setStatus(_B)
ciscoPingCompletion=NotificationType((1,3,6,1,4,1,9,9,16,2,0,1))
ciscoPingCompletion.setObjects(*((_A,_I),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoPingCompletion.setStatus(_B)
ciscoPingMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,16,3,2,3))
ciscoPingMIBNotificationGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:ciscoPingMIBNotificationGroup.setStatus(_B)
ciscoPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,16,3,1,1))
ciscoPingMIBCompliance.setObjects((_A,_b))
if mibBuilder.loadTexts:ciscoPingMIBCompliance.setStatus(_Y)
ciscoPingMIBComplianceVpn=ModuleCompliance((1,3,6,1,4,1,9,9,16,3,1,2))
ciscoPingMIBComplianceVpn.setObjects((_A,_c))
if mibBuilder.loadTexts:ciscoPingMIBComplianceVpn.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPingMIB':ciscoPingMIB,'ciscoPingMIBObjects':ciscoPingMIBObjects,'ciscoPingTable':ciscoPingTable,'ciscoPingEntry':ciscoPingEntry,_X:ciscoPingSerialNumber,_J:ciscoPingProtocol,_K:ciscoPingAddress,_L:ciscoPingPacketCount,_M:ciscoPingPacketSize,_N:ciscoPingPacketTimeout,_O:ciscoPingDelay,_P:ciscoPingTrapOnCompletion,_G:ciscoPingSentPackets,_H:ciscoPingReceivedPackets,_Q:ciscoPingMinRtt,_R:ciscoPingAvgRtt,_S:ciscoPingMaxRtt,_I:ciscoPingCompleted,_T:ciscoPingEntryOwner,_U:ciscoPingEntryStatus,_Z:ciscoPingVrfName,'ciscoPingMIBTrapPrefix':ciscoPingMIBTrapPrefix,'ciscoPingMIBTraps':ciscoPingMIBTraps,_a:ciscoPingCompletion,'ciscoPingMIBConformance':ciscoPingMIBConformance,'ciscoPingMIBCompliances':ciscoPingMIBCompliances,'ciscoPingMIBCompliance':ciscoPingMIBCompliance,'ciscoPingMIBComplianceVpn':ciscoPingMIBComplianceVpn,'ciscoPingMIBGroups':ciscoPingMIBGroups,_b:ciscoPingMIBGroup,_c:ciscoPingMIBGroupVpn,'ciscoPingMIBNotificationGroup':ciscoPingMIBNotificationGroup})