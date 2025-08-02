_F='tBgpPeerNgUseSvcRoutes'
_E='bgp4PathAttrExtnEntry'
_D='tBgpPeerNgParamsExtnEntry'
_C='TruthValue'
_B='TIMETRA-SAS-BGP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgp4PathAttrEntry,=mibBuilder.importSymbols('BGP4-MIB','bgp4PathAttrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_C)
tBgpPeerNgParamsEntry,=mibBuilder.importSymbols('TIMETRA-BGP-MIB','tBgpPeerNgParamsEntry')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
timetraSASBgpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,15))
if mibBuilder.loadTexts:timetraSASBgpMIBModule.setRevisions(('1913-11-01 00:00',))
_TmnxSASBgpConformance_ObjectIdentity=ObjectIdentity
tmnxSASBgpConformance=_TmnxSASBgpConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,14))
_TmnxSASBgpGroups_ObjectIdentity=ObjectIdentity
tmnxSASBgpGroups=_TmnxSASBgpGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,14,1))
_TmnxSASBgpObjects_ObjectIdentity=ObjectIdentity
tmnxSASBgpObjects=_TmnxSASBgpObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,18))
_TBgpSASPeerObjects_ObjectIdentity=ObjectIdentity
tBgpSASPeerObjects=_TBgpSASPeerObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,18,1))
_TBgpPeerNgParamsExtnTable_Object=MibTable
tBgpPeerNgParamsExtnTable=_TBgpPeerNgParamsExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,10))
if mibBuilder.loadTexts:tBgpPeerNgParamsExtnTable.setStatus(_A)
_TBgpPeerNgParamsExtnEntry_Object=MibTableRow
tBgpPeerNgParamsExtnEntry=_TBgpPeerNgParamsExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,10,1))
if mibBuilder.loadTexts:tBgpPeerNgParamsExtnEntry.setStatus(_A)
class _TBgpPeerNgUseSvcRoutes_Type(TruthValue):defaultValue=2
_TBgpPeerNgUseSvcRoutes_Type.__name__=_C
_TBgpPeerNgUseSvcRoutes_Object=MibTableColumn
tBgpPeerNgUseSvcRoutes=_TBgpPeerNgUseSvcRoutes_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,10,1,1),_TBgpPeerNgUseSvcRoutes_Type())
tBgpPeerNgUseSvcRoutes.setMaxAccess('read-create')
if mibBuilder.loadTexts:tBgpPeerNgUseSvcRoutes.setStatus(_A)
_Bgp4PathAttrExtnTable_Object=MibTable
bgp4PathAttrExtnTable=_Bgp4PathAttrExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,11))
if mibBuilder.loadTexts:bgp4PathAttrExtnTable.setStatus(_A)
_Bgp4PathAttrExtnEntry_Object=MibTableRow
bgp4PathAttrExtnEntry=_Bgp4PathAttrExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,11,1))
if mibBuilder.loadTexts:bgp4PathAttrExtnEntry.setStatus(_A)
_Bgp4PathUseSvcRoutesOpt_Type=TruthValue
_Bgp4PathUseSvcRoutesOpt_Object=MibTableColumn
bgp4PathUseSvcRoutesOpt=_Bgp4PathUseSvcRoutesOpt_Object((1,3,6,1,4,1,6527,6,2,2,2,18,1,11,1,1),_Bgp4PathUseSvcRoutesOpt_Type())
bgp4PathUseSvcRoutesOpt.setMaxAccess('read-only')
if mibBuilder.loadTexts:bgp4PathUseSvcRoutesOpt.setStatus(_A)
tBgpPeerNgParamsEntry.registerAugmentions((_B,_D))
tBgpPeerNgParamsExtnEntry.setIndexNames(*tBgpPeerNgParamsEntry.getIndexNames())
bgp4PathAttrEntry.registerAugmentions((_B,_E))
bgp4PathAttrExtnEntry.setIndexNames(*bgp4PathAttrEntry.getIndexNames())
tmnxSASBgpGlobalV7v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,14,1,1))
tmnxSASBgpGlobalV7v0Group.setObjects((_B,_F))
if mibBuilder.loadTexts:tmnxSASBgpGlobalV7v0Group.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraSASBgpMIBModule':timetraSASBgpMIBModule,'tmnxSASBgpConformance':tmnxSASBgpConformance,'tmnxSASBgpGroups':tmnxSASBgpGroups,'tmnxSASBgpGlobalV7v0Group':tmnxSASBgpGlobalV7v0Group,'tmnxSASBgpObjects':tmnxSASBgpObjects,'tBgpSASPeerObjects':tBgpSASPeerObjects,'tBgpPeerNgParamsExtnTable':tBgpPeerNgParamsExtnTable,_D:tBgpPeerNgParamsExtnEntry,_F:tBgpPeerNgUseSvcRoutes,'bgp4PathAttrExtnTable':bgp4PathAttrExtnTable,_E:bgp4PathAttrExtnEntry,'bgp4PathUseSvcRoutesOpt':bgp4PathUseSvcRoutesOpt})