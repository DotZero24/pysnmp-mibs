_t='ciscoPrefPathConfigGroupRev1'
_s='ciscoPrefPathConfigGroup'
_r='ciscoPrefPathHWFailureNotify'
_q='cPrefPathRouteMapGlobalActive'
_p='cPrefPathHwFailureNotifEnable'
_o='cPrefPathRouteMapSetStatus'
_n='cPrefPathRouteMapSetInfoIvrNextHopVId'
_m='cPrefPathRouteMapSetInfoIntf'
_l='cPrefPathRMapMatchStatus'
_k='cPrefPathRMapSelIvrNextHopVsanId'
_j='cPrefPathRMapSelectedIntf'
_i='cPrefPathRMapSelectedPref'
_h='cPrefPathRouteMapActive'
_g='CiscoPrefPathIvrNextHopVsanId'
_f='read-write'
_e='StorageType'
_d='Unsigned32'
_c='Integer32'
_b='notifyVsanIndex'
_a='CISCO-VSAN-MIB'
_Z='ciscoPrefPathNotifyConfigGroup'
_Y='ciscoPrefPathNotifyGroup'
_X='ciscoPrefPathInfoGroup'
_W='cPrefPathRMapSetRowStatus'
_V='cPrefPathRMapMatchRowStatus'
_U='cPrefPathRouteMapRowStatus'
_T='cPrefPathRouteMapStorageType'
_S='cPrefPathRouteMapRouteActive'
_R='cPrefPathRouteMapIntfPrefStrict'
_Q='cPrefPathRMapSetIvrNextHopVsanId'
_P='cPrefPathRMapSetIntf'
_O='cPrefPathRMapSetIntfPref'
_N='cPrefPathRMapMatchDstAddrMask'
_M='cPrefPathRMapMatchDstAddr'
_L='cPrefPathRMapMatchSrcIntf'
_K='cPrefPathRMapMatchSrcAddrMask'
_J='cPrefPathRMapMatchSrcAddr'
_I='deprecated'
_H='TruthValue'
_G='read-only'
_F='cPrefPathRouteMapRouteIndex'
_E='not-accessible'
_D='cPrefPathRouteMapVsanIndex'
_C='read-create'
_B='current'
_A='CISCO-PREFERRED-PATH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId','VsanIndex')
notifyVsanIndex,=mibBuilder.importSymbols(_a,_b)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_c,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_d,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_e,'TextualConvention',_H)
ciscoPrefPathMIB=ModuleIdentity((1,3,6,1,4,1,9,9,592))
if mibBuilder.loadTexts:ciscoPrefPathMIB.setRevisions(('2006-10-26 14:44',))
class CiscoPrefPathFcAddrMask(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('full',1),('domainArea',2),('domain',3),('noMask',4)))
class CiscoPrefPathStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('active',2),('pending',3),('deleted',4),('changed',5)))
class CiscoPrefPathIvrNextHopVsanId(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4093))
class CiscoPrefPathPreferenceLevel(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CiscoPrefPathMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPrefPathMIBNotifs=_CiscoPrefPathMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,592,0))
_CiscoPrefPathMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPrefPathMIBObjects=_CiscoPrefPathMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,592,1))
_CiscoPrefPathConfiguration_ObjectIdentity=ObjectIdentity
ciscoPrefPathConfiguration=_CiscoPrefPathConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,592,1,1))
_CPrefPathRouteMapTable_Object=MibTable
cPrefPathRouteMapTable=_CPrefPathRouteMapTable_Object((1,3,6,1,4,1,9,9,592,1,1,1))
if mibBuilder.loadTexts:cPrefPathRouteMapTable.setStatus(_B)
_CPrefPathRouteMapEntry_Object=MibTableRow
cPrefPathRouteMapEntry=_CPrefPathRouteMapEntry_Object((1,3,6,1,4,1,9,9,592,1,1,1,1))
cPrefPathRouteMapEntry.setIndexNames((0,_A,_D),(0,_A,_F))
if mibBuilder.loadTexts:cPrefPathRouteMapEntry.setStatus(_B)
_CPrefPathRouteMapVsanIndex_Type=VsanIndex
_CPrefPathRouteMapVsanIndex_Object=MibTableColumn
cPrefPathRouteMapVsanIndex=_CPrefPathRouteMapVsanIndex_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,1),_CPrefPathRouteMapVsanIndex_Type())
cPrefPathRouteMapVsanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRouteMapVsanIndex.setStatus(_B)
class _CPrefPathRouteMapRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CPrefPathRouteMapRouteIndex_Type.__name__=_d
_CPrefPathRouteMapRouteIndex_Object=MibTableColumn
cPrefPathRouteMapRouteIndex=_CPrefPathRouteMapRouteIndex_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,2),_CPrefPathRouteMapRouteIndex_Type())
cPrefPathRouteMapRouteIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRouteMapRouteIndex.setStatus(_B)
class _CPrefPathRouteMapIntfPrefStrict_Type(TruthValue):defaultValue=2
_CPrefPathRouteMapIntfPrefStrict_Type.__name__=_H
_CPrefPathRouteMapIntfPrefStrict_Object=MibTableColumn
cPrefPathRouteMapIntfPrefStrict=_CPrefPathRouteMapIntfPrefStrict_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,3),_CPrefPathRouteMapIntfPrefStrict_Type())
cPrefPathRouteMapIntfPrefStrict.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRouteMapIntfPrefStrict.setStatus(_B)
class _CPrefPathRouteMapRouteActive_Type(TruthValue):defaultValue=2
_CPrefPathRouteMapRouteActive_Type.__name__=_H
_CPrefPathRouteMapRouteActive_Object=MibTableColumn
cPrefPathRouteMapRouteActive=_CPrefPathRouteMapRouteActive_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,4),_CPrefPathRouteMapRouteActive_Type())
cPrefPathRouteMapRouteActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRouteMapRouteActive.setStatus(_B)
class _CPrefPathRouteMapActive_Type(TruthValue):defaultValue=2
_CPrefPathRouteMapActive_Type.__name__=_H
_CPrefPathRouteMapActive_Object=MibTableColumn
cPrefPathRouteMapActive=_CPrefPathRouteMapActive_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,5),_CPrefPathRouteMapActive_Type())
cPrefPathRouteMapActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRouteMapActive.setStatus(_I)
class _CPrefPathRouteMapStorageType_Type(StorageType):defaultValue=2
_CPrefPathRouteMapStorageType_Type.__name__=_e
_CPrefPathRouteMapStorageType_Object=MibTableColumn
cPrefPathRouteMapStorageType=_CPrefPathRouteMapStorageType_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,6),_CPrefPathRouteMapStorageType_Type())
cPrefPathRouteMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRouteMapStorageType.setStatus(_B)
_CPrefPathRouteMapRowStatus_Type=RowStatus
_CPrefPathRouteMapRowStatus_Object=MibTableColumn
cPrefPathRouteMapRowStatus=_CPrefPathRouteMapRowStatus_Object((1,3,6,1,4,1,9,9,592,1,1,1,1,7),_CPrefPathRouteMapRowStatus_Type())
cPrefPathRouteMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRouteMapRowStatus.setStatus(_B)
_CPrefPathRouteMapGlobalTable_Object=MibTable
cPrefPathRouteMapGlobalTable=_CPrefPathRouteMapGlobalTable_Object((1,3,6,1,4,1,9,9,592,1,1,2))
if mibBuilder.loadTexts:cPrefPathRouteMapGlobalTable.setStatus(_B)
_CPrefPathRouteMapGlobalEntry_Object=MibTableRow
cPrefPathRouteMapGlobalEntry=_CPrefPathRouteMapGlobalEntry_Object((1,3,6,1,4,1,9,9,592,1,1,2,1))
cPrefPathRouteMapGlobalEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:cPrefPathRouteMapGlobalEntry.setStatus(_B)
class _CPrefPathRouteMapGlobalActive_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('partial',2),('none',3)))
_CPrefPathRouteMapGlobalActive_Type.__name__=_c
_CPrefPathRouteMapGlobalActive_Object=MibTableColumn
cPrefPathRouteMapGlobalActive=_CPrefPathRouteMapGlobalActive_Object((1,3,6,1,4,1,9,9,592,1,1,2,1,1),_CPrefPathRouteMapGlobalActive_Type())
cPrefPathRouteMapGlobalActive.setMaxAccess(_f)
if mibBuilder.loadTexts:cPrefPathRouteMapGlobalActive.setStatus(_B)
_CPrefPathRouteMapMatchTable_Object=MibTable
cPrefPathRouteMapMatchTable=_CPrefPathRouteMapMatchTable_Object((1,3,6,1,4,1,9,9,592,1,1,3))
if mibBuilder.loadTexts:cPrefPathRouteMapMatchTable.setStatus(_B)
_CPrefPathRouteMapMatchEntry_Object=MibTableRow
cPrefPathRouteMapMatchEntry=_CPrefPathRouteMapMatchEntry_Object((1,3,6,1,4,1,9,9,592,1,1,3,1))
cPrefPathRouteMapMatchEntry.setIndexNames((0,_A,_D),(0,_A,_F),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:cPrefPathRouteMapMatchEntry.setStatus(_B)
_CPrefPathRMapMatchSrcAddr_Type=FcAddressId
_CPrefPathRMapMatchSrcAddr_Object=MibTableColumn
cPrefPathRMapMatchSrcAddr=_CPrefPathRMapMatchSrcAddr_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,1),_CPrefPathRMapMatchSrcAddr_Type())
cPrefPathRMapMatchSrcAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapMatchSrcAddr.setStatus(_B)
_CPrefPathRMapMatchSrcAddrMask_Type=CiscoPrefPathFcAddrMask
_CPrefPathRMapMatchSrcAddrMask_Object=MibTableColumn
cPrefPathRMapMatchSrcAddrMask=_CPrefPathRMapMatchSrcAddrMask_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,2),_CPrefPathRMapMatchSrcAddrMask_Type())
cPrefPathRMapMatchSrcAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapMatchSrcAddrMask.setStatus(_B)
_CPrefPathRMapMatchSrcIntf_Type=InterfaceIndexOrZero
_CPrefPathRMapMatchSrcIntf_Object=MibTableColumn
cPrefPathRMapMatchSrcIntf=_CPrefPathRMapMatchSrcIntf_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,3),_CPrefPathRMapMatchSrcIntf_Type())
cPrefPathRMapMatchSrcIntf.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapMatchSrcIntf.setStatus(_B)
_CPrefPathRMapMatchDstAddr_Type=FcAddressId
_CPrefPathRMapMatchDstAddr_Object=MibTableColumn
cPrefPathRMapMatchDstAddr=_CPrefPathRMapMatchDstAddr_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,4),_CPrefPathRMapMatchDstAddr_Type())
cPrefPathRMapMatchDstAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapMatchDstAddr.setStatus(_B)
_CPrefPathRMapMatchDstAddrMask_Type=CiscoPrefPathFcAddrMask
_CPrefPathRMapMatchDstAddrMask_Object=MibTableColumn
cPrefPathRMapMatchDstAddrMask=_CPrefPathRMapMatchDstAddrMask_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,5),_CPrefPathRMapMatchDstAddrMask_Type())
cPrefPathRMapMatchDstAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapMatchDstAddrMask.setStatus(_B)
_CPrefPathRMapMatchRowStatus_Type=RowStatus
_CPrefPathRMapMatchRowStatus_Object=MibTableColumn
cPrefPathRMapMatchRowStatus=_CPrefPathRMapMatchRowStatus_Object((1,3,6,1,4,1,9,9,592,1,1,3,1,6),_CPrefPathRMapMatchRowStatus_Type())
cPrefPathRMapMatchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRMapMatchRowStatus.setStatus(_B)
_CPrefPathRouteMapSetTable_Object=MibTable
cPrefPathRouteMapSetTable=_CPrefPathRouteMapSetTable_Object((1,3,6,1,4,1,9,9,592,1,1,4))
if mibBuilder.loadTexts:cPrefPathRouteMapSetTable.setStatus(_B)
_CPrefPathRouteMapSetEntry_Object=MibTableRow
cPrefPathRouteMapSetEntry=_CPrefPathRouteMapSetEntry_Object((1,3,6,1,4,1,9,9,592,1,1,4,1))
cPrefPathRouteMapSetEntry.setIndexNames((0,_A,_D),(0,_A,_F),(0,_A,_O))
if mibBuilder.loadTexts:cPrefPathRouteMapSetEntry.setStatus(_B)
_CPrefPathRMapSetIntfPref_Type=CiscoPrefPathPreferenceLevel
_CPrefPathRMapSetIntfPref_Object=MibTableColumn
cPrefPathRMapSetIntfPref=_CPrefPathRMapSetIntfPref_Object((1,3,6,1,4,1,9,9,592,1,1,4,1,1),_CPrefPathRMapSetIntfPref_Type())
cPrefPathRMapSetIntfPref.setMaxAccess(_E)
if mibBuilder.loadTexts:cPrefPathRMapSetIntfPref.setStatus(_B)
_CPrefPathRMapSetIntf_Type=InterfaceIndex
_CPrefPathRMapSetIntf_Object=MibTableColumn
cPrefPathRMapSetIntf=_CPrefPathRMapSetIntf_Object((1,3,6,1,4,1,9,9,592,1,1,4,1,2),_CPrefPathRMapSetIntf_Type())
cPrefPathRMapSetIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRMapSetIntf.setStatus(_B)
class _CPrefPathRMapSetIvrNextHopVsanId_Type(CiscoPrefPathIvrNextHopVsanId):defaultValue=0
_CPrefPathRMapSetIvrNextHopVsanId_Type.__name__=_g
_CPrefPathRMapSetIvrNextHopVsanId_Object=MibTableColumn
cPrefPathRMapSetIvrNextHopVsanId=_CPrefPathRMapSetIvrNextHopVsanId_Object((1,3,6,1,4,1,9,9,592,1,1,4,1,3),_CPrefPathRMapSetIvrNextHopVsanId_Type())
cPrefPathRMapSetIvrNextHopVsanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRMapSetIvrNextHopVsanId.setStatus(_B)
_CPrefPathRMapSetRowStatus_Type=RowStatus
_CPrefPathRMapSetRowStatus_Object=MibTableColumn
cPrefPathRMapSetRowStatus=_CPrefPathRMapSetRowStatus_Object((1,3,6,1,4,1,9,9,592,1,1,4,1,4),_CPrefPathRMapSetRowStatus_Type())
cPrefPathRMapSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cPrefPathRMapSetRowStatus.setStatus(_B)
_CPrefPathHwFailureNotifEnable_Type=TruthValue
_CPrefPathHwFailureNotifEnable_Object=MibScalar
cPrefPathHwFailureNotifEnable=_CPrefPathHwFailureNotifEnable_Object((1,3,6,1,4,1,9,9,592,1,1,5),_CPrefPathHwFailureNotifEnable_Type())
cPrefPathHwFailureNotifEnable.setMaxAccess(_f)
if mibBuilder.loadTexts:cPrefPathHwFailureNotifEnable.setStatus(_B)
_CiscoPrefPathInformation_ObjectIdentity=ObjectIdentity
ciscoPrefPathInformation=_CiscoPrefPathInformation_ObjectIdentity((1,3,6,1,4,1,9,9,592,1,2))
_CPrefPathRouteMapInfoTable_Object=MibTable
cPrefPathRouteMapInfoTable=_CPrefPathRouteMapInfoTable_Object((1,3,6,1,4,1,9,9,592,1,2,1))
if mibBuilder.loadTexts:cPrefPathRouteMapInfoTable.setStatus(_B)
_CPrefPathRouteMapInfoEntry_Object=MibTableRow
cPrefPathRouteMapInfoEntry=_CPrefPathRouteMapInfoEntry_Object((1,3,6,1,4,1,9,9,592,1,2,1,1))
cPrefPathRouteMapInfoEntry.setIndexNames((0,_A,_D),(0,_A,_F))
if mibBuilder.loadTexts:cPrefPathRouteMapInfoEntry.setStatus(_B)
_CPrefPathRMapSelectedPref_Type=CiscoPrefPathPreferenceLevel
_CPrefPathRMapSelectedPref_Object=MibTableColumn
cPrefPathRMapSelectedPref=_CPrefPathRMapSelectedPref_Object((1,3,6,1,4,1,9,9,592,1,2,1,1,1),_CPrefPathRMapSelectedPref_Type())
cPrefPathRMapSelectedPref.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRMapSelectedPref.setStatus(_B)
_CPrefPathRMapSelectedIntf_Type=InterfaceIndex
_CPrefPathRMapSelectedIntf_Object=MibTableColumn
cPrefPathRMapSelectedIntf=_CPrefPathRMapSelectedIntf_Object((1,3,6,1,4,1,9,9,592,1,2,1,1,2),_CPrefPathRMapSelectedIntf_Type())
cPrefPathRMapSelectedIntf.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRMapSelectedIntf.setStatus(_B)
_CPrefPathRMapSelIvrNextHopVsanId_Type=CiscoPrefPathIvrNextHopVsanId
_CPrefPathRMapSelIvrNextHopVsanId_Object=MibTableColumn
cPrefPathRMapSelIvrNextHopVsanId=_CPrefPathRMapSelIvrNextHopVsanId_Object((1,3,6,1,4,1,9,9,592,1,2,1,1,3),_CPrefPathRMapSelIvrNextHopVsanId_Type())
cPrefPathRMapSelIvrNextHopVsanId.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRMapSelIvrNextHopVsanId.setStatus(_B)
_CPrefPathRouteMapMatchInfoTable_Object=MibTable
cPrefPathRouteMapMatchInfoTable=_CPrefPathRouteMapMatchInfoTable_Object((1,3,6,1,4,1,9,9,592,1,2,2))
if mibBuilder.loadTexts:cPrefPathRouteMapMatchInfoTable.setStatus(_B)
_CPrefPathRouteMapMatchInfoEntry_Object=MibTableRow
cPrefPathRouteMapMatchInfoEntry=_CPrefPathRouteMapMatchInfoEntry_Object((1,3,6,1,4,1,9,9,592,1,2,2,1))
cPrefPathRouteMapMatchInfoEntry.setIndexNames((0,_A,_D),(0,_A,_F),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:cPrefPathRouteMapMatchInfoEntry.setStatus(_B)
_CPrefPathRMapMatchStatus_Type=CiscoPrefPathStatus
_CPrefPathRMapMatchStatus_Object=MibTableColumn
cPrefPathRMapMatchStatus=_CPrefPathRMapMatchStatus_Object((1,3,6,1,4,1,9,9,592,1,2,2,1,1),_CPrefPathRMapMatchStatus_Type())
cPrefPathRMapMatchStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRMapMatchStatus.setStatus(_B)
_CPrefPathRouteMapSetInfoTable_Object=MibTable
cPrefPathRouteMapSetInfoTable=_CPrefPathRouteMapSetInfoTable_Object((1,3,6,1,4,1,9,9,592,1,2,3))
if mibBuilder.loadTexts:cPrefPathRouteMapSetInfoTable.setStatus(_B)
_CPrefPathRouteMapSetInfoEntry_Object=MibTableRow
cPrefPathRouteMapSetInfoEntry=_CPrefPathRouteMapSetInfoEntry_Object((1,3,6,1,4,1,9,9,592,1,2,3,1))
cPrefPathRouteMapSetInfoEntry.setIndexNames((0,_A,_D),(0,_A,_F),(0,_A,_O))
if mibBuilder.loadTexts:cPrefPathRouteMapSetInfoEntry.setStatus(_B)
_CPrefPathRouteMapSetInfoIntf_Type=InterfaceIndex
_CPrefPathRouteMapSetInfoIntf_Object=MibTableColumn
cPrefPathRouteMapSetInfoIntf=_CPrefPathRouteMapSetInfoIntf_Object((1,3,6,1,4,1,9,9,592,1,2,3,1,1),_CPrefPathRouteMapSetInfoIntf_Type())
cPrefPathRouteMapSetInfoIntf.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRouteMapSetInfoIntf.setStatus(_B)
_CPrefPathRouteMapSetInfoIvrNextHopVId_Type=CiscoPrefPathIvrNextHopVsanId
_CPrefPathRouteMapSetInfoIvrNextHopVId_Object=MibTableColumn
cPrefPathRouteMapSetInfoIvrNextHopVId=_CPrefPathRouteMapSetInfoIvrNextHopVId_Object((1,3,6,1,4,1,9,9,592,1,2,3,1,2),_CPrefPathRouteMapSetInfoIvrNextHopVId_Type())
cPrefPathRouteMapSetInfoIvrNextHopVId.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRouteMapSetInfoIvrNextHopVId.setStatus(_B)
_CPrefPathRouteMapSetStatus_Type=CiscoPrefPathStatus
_CPrefPathRouteMapSetStatus_Object=MibTableColumn
cPrefPathRouteMapSetStatus=_CPrefPathRouteMapSetStatus_Object((1,3,6,1,4,1,9,9,592,1,2,3,1,3),_CPrefPathRouteMapSetStatus_Type())
cPrefPathRouteMapSetStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cPrefPathRouteMapSetStatus.setStatus(_B)
_CiscoPrefPathMIBConform_ObjectIdentity=ObjectIdentity
ciscoPrefPathMIBConform=_CiscoPrefPathMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,592,2))
_CiscoPrefPathMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPrefPathMIBCompliances=_CiscoPrefPathMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,592,2,1))
_CiscoPrefPathMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPrefPathMIBGroups=_CiscoPrefPathMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,592,2,2))
ciscoPrefPathConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,592,2,2,1))
ciscoPrefPathConfigGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_h),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoPrefPathConfigGroup.setStatus(_I)
ciscoPrefPathInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,592,2,2,2))
ciscoPrefPathInfoGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoPrefPathInfoGroup.setStatus(_B)
ciscoPrefPathNotifyConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,592,2,2,4))
ciscoPrefPathNotifyConfigGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:ciscoPrefPathNotifyConfigGroup.setStatus(_B)
ciscoPrefPathConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,592,2,2,5))
ciscoPrefPathConfigGroupRev1.setObjects(*((_A,_q),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoPrefPathConfigGroupRev1.setStatus(_B)
ciscoPrefPathHWFailureNotify=NotificationType((1,3,6,1,4,1,9,9,592,0,1))
ciscoPrefPathHWFailureNotify.setObjects((_a,_b))
if mibBuilder.loadTexts:ciscoPrefPathHWFailureNotify.setStatus(_B)
ciscoPrefPathNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,592,2,2,3))
ciscoPrefPathNotifyGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:ciscoPrefPathNotifyGroup.setStatus(_B)
ciscoPrefPathMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,592,2,1,1))
ciscoPrefPathMIBCompliance.setObjects(*((_A,_s),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoPrefPathMIBCompliance.setStatus(_I)
ciscoPrefPathMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,592,2,1,2))
ciscoPrefPathMIBComplianceRev1.setObjects(*((_A,_t),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoPrefPathMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoPrefPathFcAddrMask':CiscoPrefPathFcAddrMask,'CiscoPrefPathStatus':CiscoPrefPathStatus,_g:CiscoPrefPathIvrNextHopVsanId,'CiscoPrefPathPreferenceLevel':CiscoPrefPathPreferenceLevel,'ciscoPrefPathMIB':ciscoPrefPathMIB,'ciscoPrefPathMIBNotifs':ciscoPrefPathMIBNotifs,_r:ciscoPrefPathHWFailureNotify,'ciscoPrefPathMIBObjects':ciscoPrefPathMIBObjects,'ciscoPrefPathConfiguration':ciscoPrefPathConfiguration,'cPrefPathRouteMapTable':cPrefPathRouteMapTable,'cPrefPathRouteMapEntry':cPrefPathRouteMapEntry,_D:cPrefPathRouteMapVsanIndex,_F:cPrefPathRouteMapRouteIndex,_R:cPrefPathRouteMapIntfPrefStrict,_S:cPrefPathRouteMapRouteActive,_h:cPrefPathRouteMapActive,_T:cPrefPathRouteMapStorageType,_U:cPrefPathRouteMapRowStatus,'cPrefPathRouteMapGlobalTable':cPrefPathRouteMapGlobalTable,'cPrefPathRouteMapGlobalEntry':cPrefPathRouteMapGlobalEntry,_q:cPrefPathRouteMapGlobalActive,'cPrefPathRouteMapMatchTable':cPrefPathRouteMapMatchTable,'cPrefPathRouteMapMatchEntry':cPrefPathRouteMapMatchEntry,_J:cPrefPathRMapMatchSrcAddr,_K:cPrefPathRMapMatchSrcAddrMask,_L:cPrefPathRMapMatchSrcIntf,_M:cPrefPathRMapMatchDstAddr,_N:cPrefPathRMapMatchDstAddrMask,_V:cPrefPathRMapMatchRowStatus,'cPrefPathRouteMapSetTable':cPrefPathRouteMapSetTable,'cPrefPathRouteMapSetEntry':cPrefPathRouteMapSetEntry,_O:cPrefPathRMapSetIntfPref,_P:cPrefPathRMapSetIntf,_Q:cPrefPathRMapSetIvrNextHopVsanId,_W:cPrefPathRMapSetRowStatus,_p:cPrefPathHwFailureNotifEnable,'ciscoPrefPathInformation':ciscoPrefPathInformation,'cPrefPathRouteMapInfoTable':cPrefPathRouteMapInfoTable,'cPrefPathRouteMapInfoEntry':cPrefPathRouteMapInfoEntry,_i:cPrefPathRMapSelectedPref,_j:cPrefPathRMapSelectedIntf,_k:cPrefPathRMapSelIvrNextHopVsanId,'cPrefPathRouteMapMatchInfoTable':cPrefPathRouteMapMatchInfoTable,'cPrefPathRouteMapMatchInfoEntry':cPrefPathRouteMapMatchInfoEntry,_l:cPrefPathRMapMatchStatus,'cPrefPathRouteMapSetInfoTable':cPrefPathRouteMapSetInfoTable,'cPrefPathRouteMapSetInfoEntry':cPrefPathRouteMapSetInfoEntry,_m:cPrefPathRouteMapSetInfoIntf,_n:cPrefPathRouteMapSetInfoIvrNextHopVId,_o:cPrefPathRouteMapSetStatus,'ciscoPrefPathMIBConform':ciscoPrefPathMIBConform,'ciscoPrefPathMIBCompliances':ciscoPrefPathMIBCompliances,'ciscoPrefPathMIBCompliance':ciscoPrefPathMIBCompliance,'ciscoPrefPathMIBComplianceRev1':ciscoPrefPathMIBComplianceRev1,'ciscoPrefPathMIBGroups':ciscoPrefPathMIBGroups,_s:ciscoPrefPathConfigGroup,_X:ciscoPrefPathInfoGroup,_Y:ciscoPrefPathNotifyGroup,_Z:ciscoPrefPathNotifyConfigGroup,_t:ciscoPrefPathConfigGroupRev1})