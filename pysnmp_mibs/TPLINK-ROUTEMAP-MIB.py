_K='tpBindVid'
_J='tpRouteMapBindName'
_I='tpIpPrefixSeq'
_H='tpIpPrefixName'
_G='tpRuleId'
_F='tpRouteMapName'
_E='read-only'
_D='TPLINK-ROUTEMAP-MIB'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkRouteMapMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,76))
if mibBuilder.loadTexts:tplinkRouteMapMIB.setRevisions(('2012-12-13 09:30',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class TPRouteMapMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_TplinkRouteMapMIBObjects_ObjectIdentity=ObjectIdentity
tplinkRouteMapMIBObjects=_TplinkRouteMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,76,1))
_TpIpPrefixConfig_ObjectIdentity=ObjectIdentity
tpIpPrefixConfig=_TpIpPrefixConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,76,1,1))
_TpIpPrefixConfigTable_Object=MibTable
tpIpPrefixConfigTable=_TpIpPrefixConfigTable_Object((1,3,6,1,4,1,11863,6,76,1,1,1))
if mibBuilder.loadTexts:tpIpPrefixConfigTable.setStatus(_A)
_TpIpPrefixConfigEntry_Object=MibTableRow
tpIpPrefixConfigEntry=_TpIpPrefixConfigEntry_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1))
tpIpPrefixConfigEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:tpIpPrefixConfigEntry.setStatus(_A)
class _TpIpPrefixName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpIpPrefixName_Type.__name__=_C
_TpIpPrefixName_Object=MibTableColumn
tpIpPrefixName=_TpIpPrefixName_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,1),_TpIpPrefixName_Type())
tpIpPrefixName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpPrefixName.setStatus(_A)
_TpIpPrefixMode_Type=TPRouteMapMode
_TpIpPrefixMode_Object=MibTableColumn
tpIpPrefixMode=_TpIpPrefixMode_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,2),_TpIpPrefixMode_Type())
tpIpPrefixMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpPrefixMode.setStatus(_A)
_TpIpPrefixSeq_Type=Integer32
_TpIpPrefixSeq_Object=MibTableColumn
tpIpPrefixSeq=_TpIpPrefixSeq_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,3),_TpIpPrefixSeq_Type())
tpIpPrefixSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpPrefixSeq.setStatus(_A)
class _TpNetwork_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_TpNetwork_Type.__name__=_C
_TpNetwork_Object=MibTableColumn
tpNetwork=_TpNetwork_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,4),_TpNetwork_Type())
tpNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:tpNetwork.setStatus(_A)
_TpMaskGe_Type=Integer32
_TpMaskGe_Object=MibTableColumn
tpMaskGe=_TpMaskGe_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,5),_TpMaskGe_Type())
tpMaskGe.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMaskGe.setStatus(_A)
_TpMaskLe_Type=Integer32
_TpMaskLe_Object=MibTableColumn
tpMaskLe=_TpMaskLe_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,6),_TpMaskLe_Type())
tpMaskLe.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMaskLe.setStatus(_A)
_TpIpPrefixItemStatus_Type=TPRowStatus
_TpIpPrefixItemStatus_Object=MibTableColumn
tpIpPrefixItemStatus=_TpIpPrefixItemStatus_Object((1,3,6,1,4,1,11863,6,76,1,1,1,1,7),_TpIpPrefixItemStatus_Type())
tpIpPrefixItemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpPrefixItemStatus.setStatus(_A)
_TpRouteMapConfig_ObjectIdentity=ObjectIdentity
tpRouteMapConfig=_TpRouteMapConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,76,1,2))
_TpRouteMapConfigTable_Object=MibTable
tpRouteMapConfigTable=_TpRouteMapConfigTable_Object((1,3,6,1,4,1,11863,6,76,1,2,1))
if mibBuilder.loadTexts:tpRouteMapConfigTable.setStatus(_A)
_TpRouteMapConfigEntry_Object=MibTableRow
tpRouteMapConfigEntry=_TpRouteMapConfigEntry_Object((1,3,6,1,4,1,11863,6,76,1,2,1,1))
tpRouteMapConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:tpRouteMapConfigEntry.setStatus(_A)
class _TpRouteMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpRouteMapName_Type.__name__=_C
_TpRouteMapName_Object=MibTableColumn
tpRouteMapName=_TpRouteMapName_Object((1,3,6,1,4,1,11863,6,76,1,2,1,1,1),_TpRouteMapName_Type())
tpRouteMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpRouteMapName.setStatus(_A)
_TpConfigMode_Type=TPRouteMapMode
_TpConfigMode_Object=MibTableColumn
tpConfigMode=_TpConfigMode_Object((1,3,6,1,4,1,11863,6,76,1,2,1,1,2),_TpConfigMode_Type())
tpConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpConfigMode.setStatus(_A)
_TpRuleId_Type=Integer32
_TpRuleId_Object=MibTableColumn
tpRuleId=_TpRuleId_Object((1,3,6,1,4,1,11863,6,76,1,2,1,1,3),_TpRuleId_Type())
tpRuleId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpRuleId.setStatus(_A)
_TpConfigItemStatus_Type=TPRowStatus
_TpConfigItemStatus_Object=MibTableColumn
tpConfigItemStatus=_TpConfigItemStatus_Object((1,3,6,1,4,1,11863,6,76,1,2,1,1,4),_TpConfigItemStatus_Type())
tpConfigItemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpConfigItemStatus.setStatus(_A)
_TpRouteMapMatchConfigTable_Object=MibTable
tpRouteMapMatchConfigTable=_TpRouteMapMatchConfigTable_Object((1,3,6,1,4,1,11863,6,76,1,2,2))
if mibBuilder.loadTexts:tpRouteMapMatchConfigTable.setStatus(_A)
_TpRouteMapMatchConfigEntry_Object=MibTableRow
tpRouteMapMatchConfigEntry=_TpRouteMapMatchConfigEntry_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1))
tpRouteMapMatchConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:tpRouteMapMatchConfigEntry.setStatus(_A)
_TpMatchMode_Type=TPRouteMapMode
_TpMatchMode_Object=MibTableColumn
tpMatchMode=_TpMatchMode_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,1),_TpMatchMode_Type())
tpMatchMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMatchMode.setStatus(_A)
class _TpSIPAcl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpSIPAcl_Type.__name__=_C
_TpSIPAcl_Object=MibTableColumn
tpSIPAcl=_TpSIPAcl_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,2),_TpSIPAcl_Type())
tpSIPAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSIPAcl.setStatus(_A)
class _TpSIPPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpSIPPrefixList_Type.__name__=_C
_TpSIPPrefixList_Object=MibTableColumn
tpSIPPrefixList=_TpSIPPrefixList_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,3),_TpSIPPrefixList_Type())
tpSIPPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSIPPrefixList.setStatus(_A)
class _TpDIPAcl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpDIPAcl_Type.__name__=_C
_TpDIPAcl_Object=MibTableColumn
tpDIPAcl=_TpDIPAcl_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,4),_TpDIPAcl_Type())
tpDIPAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDIPAcl.setStatus(_A)
class _TpDIPPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpDIPPrefixList_Type.__name__=_C
_TpDIPPrefixList_Object=MibTableColumn
tpDIPPrefixList=_TpDIPPrefixList_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,5),_TpDIPPrefixList_Type())
tpDIPPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDIPPrefixList.setStatus(_A)
class _TpNXPAcl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpNXPAcl_Type.__name__=_C
_TpNXPAcl_Object=MibTableColumn
tpNXPAcl=_TpNXPAcl_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,6),_TpNXPAcl_Type())
tpNXPAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:tpNXPAcl.setStatus(_A)
class _TpNXPPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TpNXPPrefixList_Type.__name__=_C
_TpNXPPrefixList_Object=MibTableColumn
tpNXPPrefixList=_TpNXPPrefixList_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,7),_TpNXPPrefixList_Type())
tpNXPPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:tpNXPPrefixList.setStatus(_A)
_TpMatchMetric_Type=Integer32
_TpMatchMetric_Object=MibTableColumn
tpMatchMetric=_TpMatchMetric_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,8),_TpMatchMetric_Type())
tpMatchMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMatchMetric.setStatus(_A)
_TpMatchItemStatus_Type=TPRowStatus
_TpMatchItemStatus_Object=MibTableColumn
tpMatchItemStatus=_TpMatchItemStatus_Object((1,3,6,1,4,1,11863,6,76,1,2,2,1,9),_TpMatchItemStatus_Type())
tpMatchItemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMatchItemStatus.setStatus(_A)
_TpRouteMapSetConfigTable_Object=MibTable
tpRouteMapSetConfigTable=_TpRouteMapSetConfigTable_Object((1,3,6,1,4,1,11863,6,76,1,2,3))
if mibBuilder.loadTexts:tpRouteMapSetConfigTable.setStatus(_A)
_TpRouteMapSetConfigEntry_Object=MibTableRow
tpRouteMapSetConfigEntry=_TpRouteMapSetConfigEntry_Object((1,3,6,1,4,1,11863,6,76,1,2,3,1))
tpRouteMapSetConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:tpRouteMapSetConfigEntry.setStatus(_A)
_TpSetMode_Type=TPRouteMapMode
_TpSetMode_Object=MibTableColumn
tpSetMode=_TpSetMode_Object((1,3,6,1,4,1,11863,6,76,1,2,3,1,1),_TpSetMode_Type())
tpSetMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSetMode.setStatus(_A)
_TpSetMetric_Type=Integer32
_TpSetMetric_Object=MibTableColumn
tpSetMetric=_TpSetMetric_Object((1,3,6,1,4,1,11863,6,76,1,2,3,1,2),_TpSetMetric_Type())
tpSetMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSetMetric.setStatus(_A)
_TpSetNexthop_Type=IpAddress
_TpSetNexthop_Object=MibTableColumn
tpSetNexthop=_TpSetNexthop_Object((1,3,6,1,4,1,11863,6,76,1,2,3,1,3),_TpSetNexthop_Type())
tpSetNexthop.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSetNexthop.setStatus(_A)
_TpSetItemStatus_Type=TPRowStatus
_TpSetItemStatus_Object=MibTableColumn
tpSetItemStatus=_TpSetItemStatus_Object((1,3,6,1,4,1,11863,6,76,1,2,3,1,4),_TpSetItemStatus_Type())
tpSetItemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSetItemStatus.setStatus(_A)
_TpRouteMapBindConfig_ObjectIdentity=ObjectIdentity
tpRouteMapBindConfig=_TpRouteMapBindConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,76,1,3))
_TpRouteMapBindConfigTable_Object=MibTable
tpRouteMapBindConfigTable=_TpRouteMapBindConfigTable_Object((1,3,6,1,4,1,11863,6,76,1,3,1))
if mibBuilder.loadTexts:tpRouteMapBindConfigTable.setStatus(_A)
_TpRouteMapBindConfigEntry_Object=MibTableRow
tpRouteMapBindConfigEntry=_TpRouteMapBindConfigEntry_Object((1,3,6,1,4,1,11863,6,76,1,3,1,1))
tpRouteMapBindConfigEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:tpRouteMapBindConfigEntry.setStatus(_A)
class _TpRouteMapBindName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpRouteMapBindName_Type.__name__=_C
_TpRouteMapBindName_Object=MibTableColumn
tpRouteMapBindName=_TpRouteMapBindName_Object((1,3,6,1,4,1,11863,6,76,1,3,1,1,1),_TpRouteMapBindName_Type())
tpRouteMapBindName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpRouteMapBindName.setStatus(_A)
_TpBindVid_Type=Integer32
_TpBindVid_Object=MibTableColumn
tpBindVid=_TpBindVid_Object((1,3,6,1,4,1,11863,6,76,1,3,1,1,2),_TpBindVid_Type())
tpBindVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpBindVid.setStatus(_A)
_TpBindItemStatus_Type=TPRowStatus
_TpBindItemStatus_Object=MibTableColumn
tpBindItemStatus=_TpBindItemStatus_Object((1,3,6,1,4,1,11863,6,76,1,3,1,1,3),_TpBindItemStatus_Type())
tpBindItemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpBindItemStatus.setStatus(_A)
_TplinkRouteMapNotifications_ObjectIdentity=ObjectIdentity
tplinkRouteMapNotifications=_TplinkRouteMapNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,76,2))
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'TPRouteMapMode':TPRouteMapMode,'tplinkRouteMapMIB':tplinkRouteMapMIB,'tplinkRouteMapMIBObjects':tplinkRouteMapMIBObjects,'tpIpPrefixConfig':tpIpPrefixConfig,'tpIpPrefixConfigTable':tpIpPrefixConfigTable,'tpIpPrefixConfigEntry':tpIpPrefixConfigEntry,_H:tpIpPrefixName,'tpIpPrefixMode':tpIpPrefixMode,_I:tpIpPrefixSeq,'tpNetwork':tpNetwork,'tpMaskGe':tpMaskGe,'tpMaskLe':tpMaskLe,'tpIpPrefixItemStatus':tpIpPrefixItemStatus,'tpRouteMapConfig':tpRouteMapConfig,'tpRouteMapConfigTable':tpRouteMapConfigTable,'tpRouteMapConfigEntry':tpRouteMapConfigEntry,_F:tpRouteMapName,'tpConfigMode':tpConfigMode,_G:tpRuleId,'tpConfigItemStatus':tpConfigItemStatus,'tpRouteMapMatchConfigTable':tpRouteMapMatchConfigTable,'tpRouteMapMatchConfigEntry':tpRouteMapMatchConfigEntry,'tpMatchMode':tpMatchMode,'tpSIPAcl':tpSIPAcl,'tpSIPPrefixList':tpSIPPrefixList,'tpDIPAcl':tpDIPAcl,'tpDIPPrefixList':tpDIPPrefixList,'tpNXPAcl':tpNXPAcl,'tpNXPPrefixList':tpNXPPrefixList,'tpMatchMetric':tpMatchMetric,'tpMatchItemStatus':tpMatchItemStatus,'tpRouteMapSetConfigTable':tpRouteMapSetConfigTable,'tpRouteMapSetConfigEntry':tpRouteMapSetConfigEntry,'tpSetMode':tpSetMode,'tpSetMetric':tpSetMetric,'tpSetNexthop':tpSetNexthop,'tpSetItemStatus':tpSetItemStatus,'tpRouteMapBindConfig':tpRouteMapBindConfig,'tpRouteMapBindConfigTable':tpRouteMapBindConfigTable,'tpRouteMapBindConfigEntry':tpRouteMapBindConfigEntry,_J:tpRouteMapBindName,_K:tpBindVid,'tpBindItemStatus':tpBindItemStatus,'tplinkRouteMapNotifications':tplinkRouteMapNotifications})