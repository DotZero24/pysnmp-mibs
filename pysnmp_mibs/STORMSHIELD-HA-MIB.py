_K='snsNodeFanIndex'
_J='snsNodeCpuIndex'
_I='snsNodeDiskIndex'
_H='snsNodePowerSupplyIndex'
_G='Unsigned32'
_F='not-accessible'
_E='snsNodeIndex'
_D='Integer32'
_C='STORMSHIELD-HA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsHA=ModuleIdentity((1,3,6,1,4,1,11256,1,11))
if mibBuilder.loadTexts:snsHA.setRevisions(('2017-02-20 00:00',))
_SnsNbNode_Type=Integer32
_SnsNbNode_Object=MibScalar
snsNbNode=_SnsNbNode_Object((1,3,6,1,4,1,11256,1,11,1),_SnsNbNode_Type())
snsNbNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNbNode.setStatus(_A)
_SnsNbDeadNode_Type=Integer32
_SnsNbDeadNode_Object=MibScalar
snsNbDeadNode=_SnsNbDeadNode_Object((1,3,6,1,4,1,11256,1,11,2),_SnsNbDeadNode_Type())
snsNbDeadNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNbDeadNode.setStatus(_A)
_SnsNbActiveNode_Type=Integer32
_SnsNbActiveNode_Object=MibScalar
snsNbActiveNode=_SnsNbActiveNode_Object((1,3,6,1,4,1,11256,1,11,3),_SnsNbActiveNode_Type())
snsNbActiveNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNbActiveNode.setStatus(_A)
_SnsNbHALinks_Type=Integer32
_SnsNbHALinks_Object=MibScalar
snsNbHALinks=_SnsNbHALinks_Object((1,3,6,1,4,1,11256,1,11,5),_SnsNbHALinks_Type())
snsNbHALinks.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNbHALinks.setStatus(_A)
_SnsNbFaultyHALinks_Type=Integer32
_SnsNbFaultyHALinks_Object=MibScalar
snsNbFaultyHALinks=_SnsNbFaultyHALinks_Object((1,3,6,1,4,1,11256,1,11,6),_SnsNbFaultyHALinks_Type())
snsNbFaultyHALinks.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNbFaultyHALinks.setStatus(_A)
_SnsNodeTable_Object=MibTable
snsNodeTable=_SnsNodeTable_Object((1,3,6,1,4,1,11256,1,11,7))
if mibBuilder.loadTexts:snsNodeTable.setStatus(_A)
_SnsNode_Object=MibTableRow
snsNode=_SnsNode_Object((1,3,6,1,4,1,11256,1,11,7,1))
snsNode.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:snsNode.setStatus(_A)
class _SnsNodeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SnsNodeIndex_Type.__name__=_D
_SnsNodeIndex_Object=MibTableColumn
snsNodeIndex=_SnsNodeIndex_Object((1,3,6,1,4,1,11256,1,11,7,1,1),_SnsNodeIndex_Type())
snsNodeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsNodeIndex.setStatus(_A)
_SnsFwSerial_Type=DisplayString
_SnsFwSerial_Object=MibTableColumn
snsFwSerial=_SnsFwSerial_Object((1,3,6,1,4,1,11256,1,11,7,1,2),_SnsFwSerial_Type())
snsFwSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:snsFwSerial.setStatus(_A)
_SnsOnline_Type=TruthValue
_SnsOnline_Object=MibTableColumn
snsOnline=_SnsOnline_Object((1,3,6,1,4,1,11256,1,11,7,1,3),_SnsOnline_Type())
snsOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:snsOnline.setStatus(_A)
_SnsModel_Type=DisplayString
_SnsModel_Object=MibTableColumn
snsModel=_SnsModel_Object((1,3,6,1,4,1,11256,1,11,7,1,4),_SnsModel_Type())
snsModel.setMaxAccess(_B)
if mibBuilder.loadTexts:snsModel.setStatus(_A)
_SnsVersion_Type=DisplayString
_SnsVersion_Object=MibTableColumn
snsVersion=_SnsVersion_Object((1,3,6,1,4,1,11256,1,11,7,1,5),_SnsVersion_Type())
snsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVersion.setStatus(_A)
_SnsHALicence_Type=DisplayString
_SnsHALicence_Object=MibTableColumn
snsHALicence=_SnsHALicence_Object((1,3,6,1,4,1,11256,1,11,7,1,6),_SnsHALicence_Type())
snsHALicence.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHALicence.setStatus(_A)
_SnsHAQuality_Type=Integer32
_SnsHAQuality_Object=MibTableColumn
snsHAQuality=_SnsHAQuality_Object((1,3,6,1,4,1,11256,1,11,7,1,7),_SnsHAQuality_Type())
snsHAQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHAQuality.setStatus(_A)
_SnsHAPriority_Type=Integer32
_SnsHAPriority_Object=MibTableColumn
snsHAPriority=_SnsHAPriority_Object((1,3,6,1,4,1,11256,1,11,7,1,8),_SnsHAPriority_Type())
snsHAPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHAPriority.setStatus(_A)
_SnsHAStatusForced_Type=Integer32
_SnsHAStatusForced_Object=MibTableColumn
snsHAStatusForced=_SnsHAStatusForced_Object((1,3,6,1,4,1,11256,1,11,7,1,9),_SnsHAStatusForced_Type())
snsHAStatusForced.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHAStatusForced.setStatus(_A)
_SnsHAActive_Type=TruthValue
_SnsHAActive_Object=MibTableColumn
snsHAActive=_SnsHAActive_Object((1,3,6,1,4,1,11256,1,11,7,1,10),_SnsHAActive_Type())
snsHAActive.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHAActive.setStatus(_A)
_SnsUptime_Type=Integer32
_SnsUptime_Object=MibTableColumn
snsUptime=_SnsUptime_Object((1,3,6,1,4,1,11256,1,11,7,1,11),_SnsUptime_Type())
snsUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsUptime.setStatus(_A)
_SnsHASyncStatus_Type=Integer32
_SnsHASyncStatus_Object=MibScalar
snsHASyncStatus=_SnsHASyncStatus_Object((1,3,6,1,4,1,11256,1,11,8),_SnsHASyncStatus_Type())
snsHASyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHASyncStatus.setStatus(_A)
_SnsHAFwAdminRevison_Type=DisplayString
_SnsHAFwAdminRevison_Object=MibScalar
snsHAFwAdminRevison=_SnsHAFwAdminRevison_Object((1,3,6,1,4,1,11256,1,11,9),_SnsHAFwAdminRevison_Type())
snsHAFwAdminRevison.setMaxAccess(_B)
if mibBuilder.loadTexts:snsHAFwAdminRevison.setStatus(_A)
_SnsNodePowerSupplyTable_Object=MibTable
snsNodePowerSupplyTable=_SnsNodePowerSupplyTable_Object((1,3,6,1,4,1,11256,1,11,10))
if mibBuilder.loadTexts:snsNodePowerSupplyTable.setStatus(_A)
_SnsNodePowerSupplyEntry_Object=MibTableRow
snsNodePowerSupplyEntry=_SnsNodePowerSupplyEntry_Object((1,3,6,1,4,1,11256,1,11,10,1))
snsNodePowerSupplyEntry.setIndexNames((0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:snsNodePowerSupplyEntry.setStatus(_A)
class _SnsNodePowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsNodePowerSupplyIndex_Type.__name__=_D
_SnsNodePowerSupplyIndex_Object=MibTableColumn
snsNodePowerSupplyIndex=_SnsNodePowerSupplyIndex_Object((1,3,6,1,4,1,11256,1,11,10,1,1),_SnsNodePowerSupplyIndex_Type())
snsNodePowerSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsNodePowerSupplyIndex.setStatus(_A)
_SnsNodePowerSupplyPowered_Type=TruthValue
_SnsNodePowerSupplyPowered_Object=MibTableColumn
snsNodePowerSupplyPowered=_SnsNodePowerSupplyPowered_Object((1,3,6,1,4,1,11256,1,11,10,1,2),_SnsNodePowerSupplyPowered_Type())
snsNodePowerSupplyPowered.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodePowerSupplyPowered.setStatus(_A)
_SnsNodeDiskTable_Object=MibTable
snsNodeDiskTable=_SnsNodeDiskTable_Object((1,3,6,1,4,1,11256,1,11,11))
if mibBuilder.loadTexts:snsNodeDiskTable.setStatus(_A)
_SnsNodeDiskEntry_Object=MibTableRow
snsNodeDiskEntry=_SnsNodeDiskEntry_Object((1,3,6,1,4,1,11256,1,11,11,1))
snsNodeDiskEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:snsNodeDiskEntry.setStatus(_A)
class _SnsNodeDiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsNodeDiskIndex_Type.__name__=_D
_SnsNodeDiskIndex_Object=MibTableColumn
snsNodeDiskIndex=_SnsNodeDiskIndex_Object((1,3,6,1,4,1,11256,1,11,11,1,1),_SnsNodeDiskIndex_Type())
snsNodeDiskIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsNodeDiskIndex.setStatus(_A)
_SnsNodeDiskName_Type=DisplayString
_SnsNodeDiskName_Object=MibTableColumn
snsNodeDiskName=_SnsNodeDiskName_Object((1,3,6,1,4,1,11256,1,11,11,1,2),_SnsNodeDiskName_Type())
snsNodeDiskName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeDiskName.setStatus(_A)
_SnsNodeDiskSmartResult_Type=DisplayString
_SnsNodeDiskSmartResult_Object=MibTableColumn
snsNodeDiskSmartResult=_SnsNodeDiskSmartResult_Object((1,3,6,1,4,1,11256,1,11,11,1,3),_SnsNodeDiskSmartResult_Type())
snsNodeDiskSmartResult.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeDiskSmartResult.setStatus(_A)
class _SnsNodeDiskIsRaid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SnsNodeDiskIsRaid_Type.__name__=_D
_SnsNodeDiskIsRaid_Object=MibTableColumn
snsNodeDiskIsRaid=_SnsNodeDiskIsRaid_Object((1,3,6,1,4,1,11256,1,11,11,1,4),_SnsNodeDiskIsRaid_Type())
snsNodeDiskIsRaid.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeDiskIsRaid.setStatus(_A)
_SnsNodeDiskRaidStatus_Type=DisplayString
_SnsNodeDiskRaidStatus_Object=MibTableColumn
snsNodeDiskRaidStatus=_SnsNodeDiskRaidStatus_Object((1,3,6,1,4,1,11256,1,11,11,1,5),_SnsNodeDiskRaidStatus_Type())
snsNodeDiskRaidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeDiskRaidStatus.setStatus(_A)
_SnsNodeDiskPosition_Type=DisplayString
_SnsNodeDiskPosition_Object=MibTableColumn
snsNodeDiskPosition=_SnsNodeDiskPosition_Object((1,3,6,1,4,1,11256,1,11,11,1,6),_SnsNodeDiskPosition_Type())
snsNodeDiskPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeDiskPosition.setStatus(_A)
_SnsNodeCpuTable_Object=MibTable
snsNodeCpuTable=_SnsNodeCpuTable_Object((1,3,6,1,4,1,11256,1,11,12))
if mibBuilder.loadTexts:snsNodeCpuTable.setStatus(_A)
_SnsNodeCpuEntry_Object=MibTableRow
snsNodeCpuEntry=_SnsNodeCpuEntry_Object((1,3,6,1,4,1,11256,1,11,12,1))
snsNodeCpuEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:snsNodeCpuEntry.setStatus(_A)
class _SnsNodeCpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsNodeCpuIndex_Type.__name__=_D
_SnsNodeCpuIndex_Object=MibTableColumn
snsNodeCpuIndex=_SnsNodeCpuIndex_Object((1,3,6,1,4,1,11256,1,11,12,1,1),_SnsNodeCpuIndex_Type())
snsNodeCpuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsNodeCpuIndex.setStatus(_A)
_SnsNodeCpuTemp_Type=Integer32
_SnsNodeCpuTemp_Object=MibTableColumn
snsNodeCpuTemp=_SnsNodeCpuTemp_Object((1,3,6,1,4,1,11256,1,11,12,1,2),_SnsNodeCpuTemp_Type())
snsNodeCpuTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeCpuTemp.setStatus(_A)
_SnsNodeFanTable_Object=MibTable
snsNodeFanTable=_SnsNodeFanTable_Object((1,3,6,1,4,1,11256,1,11,13))
if mibBuilder.loadTexts:snsNodeFanTable.setStatus(_A)
_SnsNodeFanEntry_Object=MibTableRow
snsNodeFanEntry=_SnsNodeFanEntry_Object((1,3,6,1,4,1,11256,1,11,13,1))
snsNodeFanEntry.setIndexNames((0,_C,_E),(0,_C,_K))
if mibBuilder.loadTexts:snsNodeFanEntry.setStatus(_A)
class _SnsNodeFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnsNodeFanIndex_Type.__name__=_D
_SnsNodeFanIndex_Object=MibTableColumn
snsNodeFanIndex=_SnsNodeFanIndex_Object((1,3,6,1,4,1,11256,1,11,13,1,1),_SnsNodeFanIndex_Type())
snsNodeFanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:snsNodeFanIndex.setStatus(_A)
_SnsNodeFanName_Type=DisplayString
_SnsNodeFanName_Object=MibTableColumn
snsNodeFanName=_SnsNodeFanName_Object((1,3,6,1,4,1,11256,1,11,13,1,2),_SnsNodeFanName_Type())
snsNodeFanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeFanName.setStatus(_A)
_SnsNodeFanStatus_Type=DisplayString
_SnsNodeFanStatus_Object=MibTableColumn
snsNodeFanStatus=_SnsNodeFanStatus_Object((1,3,6,1,4,1,11256,1,11,13,1,3),_SnsNodeFanStatus_Type())
snsNodeFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeFanStatus.setStatus(_A)
class _SnsNodeFanRpm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_SnsNodeFanRpm_Type.__name__=_G
_SnsNodeFanRpm_Object=MibTableColumn
snsNodeFanRpm=_SnsNodeFanRpm_Object((1,3,6,1,4,1,11256,1,11,13,1,4),_SnsNodeFanRpm_Type())
snsNodeFanRpm.setMaxAccess(_B)
if mibBuilder.loadTexts:snsNodeFanRpm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'snsHA':snsHA,'snsNbNode':snsNbNode,'snsNbDeadNode':snsNbDeadNode,'snsNbActiveNode':snsNbActiveNode,'snsNbHALinks':snsNbHALinks,'snsNbFaultyHALinks':snsNbFaultyHALinks,'snsNodeTable':snsNodeTable,'snsNode':snsNode,_E:snsNodeIndex,'snsFwSerial':snsFwSerial,'snsOnline':snsOnline,'snsModel':snsModel,'snsVersion':snsVersion,'snsHALicence':snsHALicence,'snsHAQuality':snsHAQuality,'snsHAPriority':snsHAPriority,'snsHAStatusForced':snsHAStatusForced,'snsHAActive':snsHAActive,'snsUptime':snsUptime,'snsHASyncStatus':snsHASyncStatus,'snsHAFwAdminRevison':snsHAFwAdminRevison,'snsNodePowerSupplyTable':snsNodePowerSupplyTable,'snsNodePowerSupplyEntry':snsNodePowerSupplyEntry,_H:snsNodePowerSupplyIndex,'snsNodePowerSupplyPowered':snsNodePowerSupplyPowered,'snsNodeDiskTable':snsNodeDiskTable,'snsNodeDiskEntry':snsNodeDiskEntry,_I:snsNodeDiskIndex,'snsNodeDiskName':snsNodeDiskName,'snsNodeDiskSmartResult':snsNodeDiskSmartResult,'snsNodeDiskIsRaid':snsNodeDiskIsRaid,'snsNodeDiskRaidStatus':snsNodeDiskRaidStatus,'snsNodeDiskPosition':snsNodeDiskPosition,'snsNodeCpuTable':snsNodeCpuTable,'snsNodeCpuEntry':snsNodeCpuEntry,_J:snsNodeCpuIndex,'snsNodeCpuTemp':snsNodeCpuTemp,'snsNodeFanTable':snsNodeFanTable,'snsNodeFanEntry':snsNodeFanEntry,_K:snsNodeFanIndex,'snsNodeFanName':snsNodeFanName,'snsNodeFanStatus':snsNodeFanStatus,'snsNodeFanRpm':snsNodeFanRpm})