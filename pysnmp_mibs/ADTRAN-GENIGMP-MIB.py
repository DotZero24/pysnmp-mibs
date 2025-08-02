_O='read-only'
_N='transparent'
_M='DisplayString'
_L='adGenEthernetDslamFlowName'
_K='ADTRAN-ETHERNET-DSLAM-FLOW-MIB'
_J='adGenSlotInfoIndex'
_I='ADTRAN-GENSLOT-MIB'
_H='adGenEVCName'
_G='ADTRAN-GENEVC-MIB'
_F='enabled'
_E='disabled'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenEthernetDslamFlowName,=mibBuilder.importSymbols(_K,_L)
adGenEVCName,=mibBuilder.importSymbols(_G,_H)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_I,_J)
adGenIGMP,adGenIGMPID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenIGMP','adGenIGMPID')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention')
adGenIGMPMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,16,1))
if mibBuilder.loadTexts:adGenIGMPMIB.setRevisions(('2013-05-02 00:00','2013-02-20 00:00','2013-02-04 00:00','2010-06-07 00:00'))
_AdGenIGMPProvisioning_ObjectIdentity=ObjectIdentity
adGenIGMPProvisioning=_AdGenIGMPProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,16,1))
_AdGenIGMPEVCTable_Object=MibTable
adGenIGMPEVCTable=_AdGenIGMPEVCTable_Object((1,3,6,1,4,1,664,5,70,16,1,1))
if mibBuilder.loadTexts:adGenIGMPEVCTable.setStatus(_A)
_AdGenIGMPEVCEntry_Object=MibTableRow
adGenIGMPEVCEntry=_AdGenIGMPEVCEntry_Object((1,3,6,1,4,1,664,5,70,16,1,1,1))
adGenIGMPEVCEntry.setIndexNames((1,_G,_H))
if mibBuilder.loadTexts:adGenIGMPEVCEntry.setStatus(_A)
class _AdGenIGMPEVCPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenIGMPEVCPriority_Type.__name__=_B
_AdGenIGMPEVCPriority_Object=MibTableColumn
adGenIGMPEVCPriority=_AdGenIGMPEVCPriority_Object((1,3,6,1,4,1,664,5,70,16,1,1,1,1),_AdGenIGMPEVCPriority_Type())
adGenIGMPEVCPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCPriority.setStatus(_A)
class _AdGenIGMPEVCVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('v2',2),('v3lite',3)))
_AdGenIGMPEVCVersion_Type.__name__=_B
_AdGenIGMPEVCVersion_Object=MibTableColumn
adGenIGMPEVCVersion=_AdGenIGMPEVCVersion_Object((1,3,6,1,4,1,664,5,70,16,1,1,1,2),_AdGenIGMPEVCVersion_Type())
adGenIGMPEVCVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCVersion.setStatus(_A)
_AdGenIGMPEVCSlotTable_Object=MibTable
adGenIGMPEVCSlotTable=_AdGenIGMPEVCSlotTable_Object((1,3,6,1,4,1,664,5,70,16,1,2))
if mibBuilder.loadTexts:adGenIGMPEVCSlotTable.setStatus(_A)
_AdGenIGMPEVCSlotEntry_Object=MibTableRow
adGenIGMPEVCSlotEntry=_AdGenIGMPEVCSlotEntry_Object((1,3,6,1,4,1,664,5,70,16,1,2,1))
adGenIGMPEVCSlotEntry.setIndexNames((0,_I,_J),(1,_G,_H))
if mibBuilder.loadTexts:adGenIGMPEVCSlotEntry.setStatus(_A)
_AdGenIGMPEVCSlotHostIP_Type=IpAddress
_AdGenIGMPEVCSlotHostIP_Object=MibTableColumn
adGenIGMPEVCSlotHostIP=_AdGenIGMPEVCSlotHostIP_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,1),_AdGenIGMPEVCSlotHostIP_Type())
adGenIGMPEVCSlotHostIP.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIGMPEVCSlotHostIP.setStatus(_A)
class _AdGenIGMPEVCSlotLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_AdGenIGMPEVCSlotLastMemberQueryInterval_Type.__name__=_B
_AdGenIGMPEVCSlotLastMemberQueryInterval_Object=MibTableColumn
adGenIGMPEVCSlotLastMemberQueryInterval=_AdGenIGMPEVCSlotLastMemberQueryInterval_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,2),_AdGenIGMPEVCSlotLastMemberQueryInterval_Type())
adGenIGMPEVCSlotLastMemberQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIGMPEVCSlotLastMemberQueryInterval.setStatus(_A)
class _AdGenIGMPEVCSlotLastMemberQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenIGMPEVCSlotLastMemberQueryCount_Type.__name__=_B
_AdGenIGMPEVCSlotLastMemberQueryCount_Object=MibTableColumn
adGenIGMPEVCSlotLastMemberQueryCount=_AdGenIGMPEVCSlotLastMemberQueryCount_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,3),_AdGenIGMPEVCSlotLastMemberQueryCount_Type())
adGenIGMPEVCSlotLastMemberQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIGMPEVCSlotLastMemberQueryCount.setStatus(_A)
class _AdGenIGMPEVCSlotMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snooping',1),('proxy',2),(_N,3)))
_AdGenIGMPEVCSlotMode_Type.__name__=_B
_AdGenIGMPEVCSlotMode_Object=MibTableColumn
adGenIGMPEVCSlotMode=_AdGenIGMPEVCSlotMode_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,4),_AdGenIGMPEVCSlotMode_Type())
adGenIGMPEVCSlotMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIGMPEVCSlotMode.setStatus(_A)
_AdGenIGMPEVCSlotRowStatus_Type=RowStatus
_AdGenIGMPEVCSlotRowStatus_Object=MibTableColumn
adGenIGMPEVCSlotRowStatus=_AdGenIGMPEVCSlotRowStatus_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,5),_AdGenIGMPEVCSlotRowStatus_Type())
adGenIGMPEVCSlotRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenIGMPEVCSlotRowStatus.setStatus(_A)
_AdGenIGMPEVCSlotStatus_Type=DisplayString
_AdGenIGMPEVCSlotStatus_Object=MibTableColumn
adGenIGMPEVCSlotStatus=_AdGenIGMPEVCSlotStatus_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,6),_AdGenIGMPEVCSlotStatus_Type())
adGenIGMPEVCSlotStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:adGenIGMPEVCSlotStatus.setStatus(_A)
_AdGenIGMPEVCSlotLastError_Type=DisplayString
_AdGenIGMPEVCSlotLastError_Object=MibTableColumn
adGenIGMPEVCSlotLastError=_AdGenIGMPEVCSlotLastError_Object((1,3,6,1,4,1,664,5,70,16,1,2,1,7),_AdGenIGMPEVCSlotLastError_Type())
adGenIGMPEVCSlotLastError.setMaxAccess(_O)
if mibBuilder.loadTexts:adGenIGMPEVCSlotLastError.setStatus(_A)
_AdGenIGMPEVCMapTable_Object=MibTable
adGenIGMPEVCMapTable=_AdGenIGMPEVCMapTable_Object((1,3,6,1,4,1,664,5,70,16,1,3))
if mibBuilder.loadTexts:adGenIGMPEVCMapTable.setStatus(_A)
_AdGenIGMPEVCMapEntry_Object=MibTableRow
adGenIGMPEVCMapEntry=_AdGenIGMPEVCMapEntry_Object((1,3,6,1,4,1,664,5,70,16,1,3,1))
adGenIGMPEVCMapEntry.setIndexNames((0,_I,_J),(1,_K,_L))
if mibBuilder.loadTexts:adGenIGMPEVCMapEntry.setStatus(_A)
class _AdGenIGMPEVCMapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('processingEnabled',1),('block',2),(_N,3),('forking',4)))
_AdGenIGMPEVCMapMode_Type.__name__=_B
_AdGenIGMPEVCMapMode_Object=MibTableColumn
adGenIGMPEVCMapMode=_AdGenIGMPEVCMapMode_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,1),_AdGenIGMPEVCMapMode_Type())
adGenIGMPEVCMapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMode.setStatus(_A)
_AdGenIGMPEVCMapMaxMulticastBandwidth_Type=Integer32
_AdGenIGMPEVCMapMaxMulticastBandwidth_Object=MibTableColumn
adGenIGMPEVCMapMaxMulticastBandwidth=_AdGenIGMPEVCMapMaxMulticastBandwidth_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,2),_AdGenIGMPEVCMapMaxMulticastBandwidth_Type())
adGenIGMPEVCMapMaxMulticastBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMaxMulticastBandwidth.setStatus(_A)
class _AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type.__name__=_B
_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Object=MibTableColumn
adGenIGMPEVCMapMaxMulticastBandwidthEnable=_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,3),_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type())
adGenIGMPEVCMapMaxMulticastBandwidthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMaxMulticastBandwidthEnable.setStatus(_A)
_AdGenIGMPEVCMapMaxMulticastGroups_Type=Integer32
_AdGenIGMPEVCMapMaxMulticastGroups_Object=MibTableColumn
adGenIGMPEVCMapMaxMulticastGroups=_AdGenIGMPEVCMapMaxMulticastGroups_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,4),_AdGenIGMPEVCMapMaxMulticastGroups_Type())
adGenIGMPEVCMapMaxMulticastGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMaxMulticastGroups.setStatus(_A)
class _AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type.__name__=_B
_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Object=MibTableColumn
adGenIGMPEVCMapMaxMulticastGroupsEnable=_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,5),_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type())
adGenIGMPEVCMapMaxMulticastGroupsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMaxMulticastGroupsEnable.setStatus(_A)
_AdGenIGMPEVCMapRouterIP_Type=IpAddress
_AdGenIGMPEVCMapRouterIP_Object=MibTableColumn
adGenIGMPEVCMapRouterIP=_AdGenIGMPEVCMapRouterIP_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,6),_AdGenIGMPEVCMapRouterIP_Type())
adGenIGMPEVCMapRouterIP.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapRouterIP.setStatus(_A)
class _AdGenIGMPEVCMapImmediateLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),('notApplicable',3)))
_AdGenIGMPEVCMapImmediateLeave_Type.__name__=_B
_AdGenIGMPEVCMapImmediateLeave_Object=MibTableColumn
adGenIGMPEVCMapImmediateLeave=_AdGenIGMPEVCMapImmediateLeave_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,7),_AdGenIGMPEVCMapImmediateLeave_Type())
adGenIGMPEVCMapImmediateLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapImmediateLeave.setStatus(_A)
class _AdGenIGMPEVCMapMulticastACLMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('permit',1),('deny',2),(_E,3)))
_AdGenIGMPEVCMapMulticastACLMode_Type.__name__=_B
_AdGenIGMPEVCMapMulticastACLMode_Object=MibTableColumn
adGenIGMPEVCMapMulticastACLMode=_AdGenIGMPEVCMapMulticastACLMode_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,8),_AdGenIGMPEVCMapMulticastACLMode_Type())
adGenIGMPEVCMapMulticastACLMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMulticastACLMode.setStatus(_A)
class _AdGenIGMPEVCMapMulticastACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenIGMPEVCMapMulticastACLName_Type.__name__=_M
_AdGenIGMPEVCMapMulticastACLName_Object=MibTableColumn
adGenIGMPEVCMapMulticastACLName=_AdGenIGMPEVCMapMulticastACLName_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,9),_AdGenIGMPEVCMapMulticastACLName_Type())
adGenIGMPEVCMapMulticastACLName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapMulticastACLName.setStatus(_A)
class _AdGenIGMPEVCMapAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_AdGenIGMPEVCMapAuthentication_Type.__name__=_B
_AdGenIGMPEVCMapAuthentication_Object=MibTableColumn
adGenIGMPEVCMapAuthentication=_AdGenIGMPEVCMapAuthentication_Object((1,3,6,1,4,1,664,5,70,16,1,3,1,10),_AdGenIGMPEVCMapAuthentication_Type())
adGenIGMPEVCMapAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIGMPEVCMapAuthentication.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENIGMP-MIB',**{'adGenIGMPProvisioning':adGenIGMPProvisioning,'adGenIGMPEVCTable':adGenIGMPEVCTable,'adGenIGMPEVCEntry':adGenIGMPEVCEntry,'adGenIGMPEVCPriority':adGenIGMPEVCPriority,'adGenIGMPEVCVersion':adGenIGMPEVCVersion,'adGenIGMPEVCSlotTable':adGenIGMPEVCSlotTable,'adGenIGMPEVCSlotEntry':adGenIGMPEVCSlotEntry,'adGenIGMPEVCSlotHostIP':adGenIGMPEVCSlotHostIP,'adGenIGMPEVCSlotLastMemberQueryInterval':adGenIGMPEVCSlotLastMemberQueryInterval,'adGenIGMPEVCSlotLastMemberQueryCount':adGenIGMPEVCSlotLastMemberQueryCount,'adGenIGMPEVCSlotMode':adGenIGMPEVCSlotMode,'adGenIGMPEVCSlotRowStatus':adGenIGMPEVCSlotRowStatus,'adGenIGMPEVCSlotStatus':adGenIGMPEVCSlotStatus,'adGenIGMPEVCSlotLastError':adGenIGMPEVCSlotLastError,'adGenIGMPEVCMapTable':adGenIGMPEVCMapTable,'adGenIGMPEVCMapEntry':adGenIGMPEVCMapEntry,'adGenIGMPEVCMapMode':adGenIGMPEVCMapMode,'adGenIGMPEVCMapMaxMulticastBandwidth':adGenIGMPEVCMapMaxMulticastBandwidth,'adGenIGMPEVCMapMaxMulticastBandwidthEnable':adGenIGMPEVCMapMaxMulticastBandwidthEnable,'adGenIGMPEVCMapMaxMulticastGroups':adGenIGMPEVCMapMaxMulticastGroups,'adGenIGMPEVCMapMaxMulticastGroupsEnable':adGenIGMPEVCMapMaxMulticastGroupsEnable,'adGenIGMPEVCMapRouterIP':adGenIGMPEVCMapRouterIP,'adGenIGMPEVCMapImmediateLeave':adGenIGMPEVCMapImmediateLeave,'adGenIGMPEVCMapMulticastACLMode':adGenIGMPEVCMapMulticastACLMode,'adGenIGMPEVCMapMulticastACLName':adGenIGMPEVCMapMulticastACLName,'adGenIGMPEVCMapAuthentication':adGenIGMPEVCMapAuthentication,'adGenIGMPMIB':adGenIGMPMIB})