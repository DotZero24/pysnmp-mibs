_W='staticMulticastGroup'
_V='unicastGroup'
_U='mpeConfigGroup'
_T='staticMulticastRowstatus'
_S='staticMulticastGroupAddress'
_R='unicastRowStatus'
_Q='unicastGatewayAddr'
_P='unicastOutputPortID'
_O='unicastMask'
_N='unicastRoute'
_M='mpeMultipacket'
_L='mpeConfigRIP'
_K='mpeConfigIGMP'
_J='mpeConfigForwarding'
_I='staticMulticastIdx'
_H='unicastIdx'
_G='mpeConfigPortID'
_F='not-accessible'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='CISCO-DMN-DSG-MPE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoDSGMPE=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,26))
if mibBuilder.loadTexts:ciscoDSGMPE.setRevisions(('2010-08-30 11:00','2010-05-07 06:30','2010-05-03 11:00','2010-04-12 06:00'))
_MpeTable_ObjectIdentity=ObjectIdentity
mpeTable=_MpeTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,26,2))
_MpeConfigTable_Object=MibTable
mpeConfigTable=_MpeConfigTable_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1))
if mibBuilder.loadTexts:mpeConfigTable.setStatus(_A)
_MpeConfigEntry_Object=MibTableRow
mpeConfigEntry=_MpeConfigEntry_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1))
mpeConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mpeConfigEntry.setStatus(_A)
class _MpeConfigPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MpeConfigPortID_Type.__name__=_C
_MpeConfigPortID_Object=MibTableColumn
mpeConfigPortID=_MpeConfigPortID_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1,1),_MpeConfigPortID_Type())
mpeConfigPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:mpeConfigPortID.setStatus(_A)
class _MpeConfigForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forwardNone',1),('forwardAll',2),('forwardFilteredList',3)))
_MpeConfigForwarding_Type.__name__=_C
_MpeConfigForwarding_Object=MibTableColumn
mpeConfigForwarding=_MpeConfigForwarding_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1,2),_MpeConfigForwarding_Type())
mpeConfigForwarding.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeConfigForwarding.setStatus(_A)
class _MpeConfigIGMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_MpeConfigIGMP_Type.__name__=_C
_MpeConfigIGMP_Object=MibTableColumn
mpeConfigIGMP=_MpeConfigIGMP_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1,3),_MpeConfigIGMP_Type())
mpeConfigIGMP.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeConfigIGMP.setStatus(_A)
class _MpeConfigRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_MpeConfigRIP_Type.__name__=_C
_MpeConfigRIP_Object=MibTableColumn
mpeConfigRIP=_MpeConfigRIP_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1,4),_MpeConfigRIP_Type())
mpeConfigRIP.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeConfigRIP.setStatus(_A)
class _MpeMultipacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,24)));namedValues=NamedValues(*(('lowerJitter',1),('higherBitRate',24)))
_MpeMultipacket_Type.__name__=_C
_MpeMultipacket_Object=MibTableColumn
mpeMultipacket=_MpeMultipacket_Object((1,3,6,1,4,1,1429,2,2,5,26,2,1,1,5),_MpeMultipacket_Type())
mpeMultipacket.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeMultipacket.setStatus(_A)
_UnicastTable_Object=MibTable
unicastTable=_UnicastTable_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2))
if mibBuilder.loadTexts:unicastTable.setStatus(_A)
_UnicastEntry_Object=MibTableRow
unicastEntry=_UnicastEntry_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1))
unicastEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:unicastEntry.setStatus(_A)
class _UnicastIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_UnicastIdx_Type.__name__=_C
_UnicastIdx_Object=MibTableColumn
unicastIdx=_UnicastIdx_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,1),_UnicastIdx_Type())
unicastIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:unicastIdx.setStatus(_A)
_UnicastRoute_Type=IpAddress
_UnicastRoute_Object=MibTableColumn
unicastRoute=_UnicastRoute_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,2),_UnicastRoute_Type())
unicastRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:unicastRoute.setStatus(_A)
class _UnicastMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,32))
_UnicastMask_Type.__name__=_C
_UnicastMask_Object=MibTableColumn
unicastMask=_UnicastMask_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,3),_UnicastMask_Type())
unicastMask.setMaxAccess(_D)
if mibBuilder.loadTexts:unicastMask.setStatus(_A)
class _UnicastOutputPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_UnicastOutputPortID_Type.__name__=_C
_UnicastOutputPortID_Object=MibTableColumn
unicastOutputPortID=_UnicastOutputPortID_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,4),_UnicastOutputPortID_Type())
unicastOutputPortID.setMaxAccess(_D)
if mibBuilder.loadTexts:unicastOutputPortID.setStatus(_A)
_UnicastGatewayAddr_Type=IpAddress
_UnicastGatewayAddr_Object=MibTableColumn
unicastGatewayAddr=_UnicastGatewayAddr_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,5),_UnicastGatewayAddr_Type())
unicastGatewayAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:unicastGatewayAddr.setStatus(_A)
_UnicastRowStatus_Type=RowStatus
_UnicastRowStatus_Object=MibTableColumn
unicastRowStatus=_UnicastRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,26,2,2,1,6),_UnicastRowStatus_Type())
unicastRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:unicastRowStatus.setStatus(_A)
_StaticMulticastTable_Object=MibTable
staticMulticastTable=_StaticMulticastTable_Object((1,3,6,1,4,1,1429,2,2,5,26,2,3))
if mibBuilder.loadTexts:staticMulticastTable.setStatus(_A)
_StaticMulticastEntry_Object=MibTableRow
staticMulticastEntry=_StaticMulticastEntry_Object((1,3,6,1,4,1,1429,2,2,5,26,2,3,1))
staticMulticastEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:staticMulticastEntry.setStatus(_A)
class _StaticMulticastIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_StaticMulticastIdx_Type.__name__=_C
_StaticMulticastIdx_Object=MibTableColumn
staticMulticastIdx=_StaticMulticastIdx_Object((1,3,6,1,4,1,1429,2,2,5,26,2,3,1,1),_StaticMulticastIdx_Type())
staticMulticastIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:staticMulticastIdx.setStatus(_A)
_StaticMulticastGroupAddress_Type=IpAddress
_StaticMulticastGroupAddress_Object=MibTableColumn
staticMulticastGroupAddress=_StaticMulticastGroupAddress_Object((1,3,6,1,4,1,1429,2,2,5,26,2,3,1,2),_StaticMulticastGroupAddress_Type())
staticMulticastGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:staticMulticastGroupAddress.setStatus(_A)
_StaticMulticastRowstatus_Type=RowStatus
_StaticMulticastRowstatus_Object=MibTableColumn
staticMulticastRowstatus=_StaticMulticastRowstatus_Object((1,3,6,1,4,1,1429,2,2,5,26,2,3,1,3),_StaticMulticastRowstatus_Type())
staticMulticastRowstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:staticMulticastRowstatus.setStatus(_A)
_MpeMIBConformance_ObjectIdentity=ObjectIdentity
mpeMIBConformance=_MpeMIBConformance_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,26,3))
_MpeMIBCompliances_ObjectIdentity=ObjectIdentity
mpeMIBCompliances=_MpeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,26,3,1))
_MpeMIBGroups_ObjectIdentity=ObjectIdentity
mpeMIBGroups=_MpeMIBGroups_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,26,3,2))
mpeConfigGroup=ObjectGroup((1,3,6,1,4,1,1429,2,2,5,26,3,2,1))
mpeConfigGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:mpeConfigGroup.setStatus(_A)
unicastGroup=ObjectGroup((1,3,6,1,4,1,1429,2,2,5,26,3,2,2))
unicastGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:unicastGroup.setStatus(_A)
staticMulticastGroup=ObjectGroup((1,3,6,1,4,1,1429,2,2,5,26,3,2,3))
staticMulticastGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:staticMulticastGroup.setStatus(_A)
mpeCompliance=ModuleCompliance((1,3,6,1,4,1,1429,2,2,5,26,3,1,1))
mpeCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:mpeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDSGMPE':ciscoDSGMPE,'mpeTable':mpeTable,'mpeConfigTable':mpeConfigTable,'mpeConfigEntry':mpeConfigEntry,_G:mpeConfigPortID,_J:mpeConfigForwarding,_K:mpeConfigIGMP,_L:mpeConfigRIP,_M:mpeMultipacket,'unicastTable':unicastTable,'unicastEntry':unicastEntry,_H:unicastIdx,_N:unicastRoute,_O:unicastMask,_P:unicastOutputPortID,_Q:unicastGatewayAddr,_R:unicastRowStatus,'staticMulticastTable':staticMulticastTable,'staticMulticastEntry':staticMulticastEntry,_I:staticMulticastIdx,_S:staticMulticastGroupAddress,_T:staticMulticastRowstatus,'mpeMIBConformance':mpeMIBConformance,'mpeMIBCompliances':mpeMIBCompliances,'mpeCompliance':mpeCompliance,'mpeMIBGroups':mpeMIBGroups,_U:mpeConfigGroup,_V:unicastGroup,_W:staticMulticastGroup})