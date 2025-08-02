_J='tMirrorDestinationMirrorSourceType'
_I='tMirrorDestinationFCProfile'
_H='tMirrorSourcePortEgressMirroringType'
_G='tMirrorDestinationExtnEntry'
_F='tMirrorSourcePortExtnEntry'
_E='TProfileOrNone'
_D='read-create'
_C='Integer32'
_B='TIMETRA-SAS-MIRROR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
TEntryId,TEntryIdOrZero,TFilterID,TFilterType=mibBuilder.importSymbols('TIMETRA-FILTER-MIB','TEntryId','TEntryIdOrZero','TFilterID','TFilterType')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tMirrorDestinationEntry,tMirrorSourcePortEntry=mibBuilder.importSymbols('TIMETRA-MIRROR-MIB','tMirrorDestinationEntry','tMirrorSourcePortEntry')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
SdpId,=mibBuilder.importSymbols('TIMETRA-SERV-MIB','SdpId')
SdpBindId,ServiceAdminStatus,ServiceOperStatus,TFCName,TFCSet,TItemDescription,TNamedItem,TNamedItemOrEmpty,TPolicyID,TProfileOrNone,TmnxEncapVal,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TIMETRA-TC-MIB','SdpBindId','ServiceAdminStatus','ServiceOperStatus','TFCName','TFCSet','TItemDescription','TNamedItem','TNamedItemOrEmpty','TPolicyID',_E,'TmnxEncapVal','TmnxPortID','TmnxServId')
timetraSASMirrorMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,13))
if mibBuilder.loadTexts:timetraSASMirrorMIBModule.setRevisions(('1911-05-01 00:00',))
_TmnxSASMirrorGroups_ObjectIdentity=ObjectIdentity
tmnxSASMirrorGroups=_TmnxSASMirrorGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,8))
_TSASMirrorObjects_ObjectIdentity=ObjectIdentity
tSASMirrorObjects=_TSASMirrorObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,13))
_TMirrorSourcePortExtnTable_Object=MibTable
tMirrorSourcePortExtnTable=_TMirrorSourcePortExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,13,1))
if mibBuilder.loadTexts:tMirrorSourcePortExtnTable.setStatus(_A)
_TMirrorSourcePortExtnEntry_Object=MibTableRow
tMirrorSourcePortExtnEntry=_TMirrorSourcePortExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,13,1,1))
if mibBuilder.loadTexts:tMirrorSourcePortExtnEntry.setStatus(_A)
class _TMirrorSourcePortEgressMirroringType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true-egress-mirroring',1),('normal-egress-mirroring',2)))
_TMirrorSourcePortEgressMirroringType_Type.__name__=_C
_TMirrorSourcePortEgressMirroringType_Object=MibTableColumn
tMirrorSourcePortEgressMirroringType=_TMirrorSourcePortEgressMirroringType_Object((1,3,6,1,4,1,6527,6,2,2,2,13,1,1,1),_TMirrorSourcePortEgressMirroringType_Type())
tMirrorSourcePortEgressMirroringType.setMaxAccess(_D)
if mibBuilder.loadTexts:tMirrorSourcePortEgressMirroringType.setStatus(_A)
_TMirrorDestinationExtnTable_Object=MibTable
tMirrorDestinationExtnTable=_TMirrorDestinationExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,13,2))
if mibBuilder.loadTexts:tMirrorDestinationExtnTable.setStatus(_A)
_TMirrorDestinationExtnEntry_Object=MibTableRow
tMirrorDestinationExtnEntry=_TMirrorDestinationExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,13,2,1))
if mibBuilder.loadTexts:tMirrorDestinationExtnEntry.setStatus(_A)
class _TMirrorDestinationFCProfile_Type(TProfileOrNone):defaultValue=2
_TMirrorDestinationFCProfile_Type.__name__=_E
_TMirrorDestinationFCProfile_Object=MibTableColumn
tMirrorDestinationFCProfile=_TMirrorDestinationFCProfile_Object((1,3,6,1,4,1,6527,6,2,2,2,13,2,1,1),_TMirrorDestinationFCProfile_Type())
tMirrorDestinationFCProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:tMirrorDestinationFCProfile.setStatus(_A)
class _TMirrorDestinationMirrorSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remote',2),('both',3)))
_TMirrorDestinationMirrorSourceType_Type.__name__=_C
_TMirrorDestinationMirrorSourceType_Object=MibTableColumn
tMirrorDestinationMirrorSourceType=_TMirrorDestinationMirrorSourceType_Object((1,3,6,1,4,1,6527,6,2,2,2,13,2,1,2),_TMirrorDestinationMirrorSourceType_Type())
tMirrorDestinationMirrorSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:tMirrorDestinationMirrorSourceType.setStatus(_A)
tMirrorSourcePortEntry.registerAugmentions((_B,_F))
tMirrorSourcePortExtnEntry.setIndexNames(*tMirrorSourcePortEntry.getIndexNames())
tMirrorDestinationEntry.registerAugmentions((_B,_G))
tMirrorDestinationExtnEntry.setIndexNames(*tMirrorDestinationEntry.getIndexNames())
tmnxSASMirrorV1v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,8,1))
tmnxSASMirrorV1v0Group.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:tmnxSASMirrorV1v0Group.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraSASMirrorMIBModule':timetraSASMirrorMIBModule,'tmnxSASMirrorGroups':tmnxSASMirrorGroups,'tmnxSASMirrorV1v0Group':tmnxSASMirrorV1v0Group,'tSASMirrorObjects':tSASMirrorObjects,'tMirrorSourcePortExtnTable':tMirrorSourcePortExtnTable,_F:tMirrorSourcePortExtnEntry,_H:tMirrorSourcePortEgressMirroringType,'tMirrorDestinationExtnTable':tMirrorDestinationExtnTable,_G:tMirrorDestinationExtnEntry,_I:tMirrorDestinationFCProfile,_J:tMirrorDestinationMirrorSourceType})