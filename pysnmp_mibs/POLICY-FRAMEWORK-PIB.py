_c='policyCompLimitsGroup'
_b='policyDeviceIdentificationGroup'
_a='policyPibIncarnationGroup'
_Z='policyPrcSupportGroup'
_Y='policyCompLimitsGuidance'
_X='policyCompLimitsType'
_W='policyCompLimitsComponent'
_V='policyDeviceIdentificationMaxMsg'
_U='policyDeviceIdentificationDescr'
_T='policyPibIncarnationActive'
_S='policyPibIncarnationTtl'
_R='policyPibIncarnationLongevity'
_Q='policyPibIncarnationId'
_P='policyPibIncarnationName'
_O='policyPrcSupportMaxPris'
_N='policyPrcSupportSupportedAttrs'
_M='policyPrcSupportSupportedPrc'
_L='policyCompLimitsPrid'
_K='policyDeviceIdentificationPrid'
_J='policyPibIncarnationPrid'
_I='policyPrcSupportPrid'
_H='Integer32'
_G='SnmpAdminString'
_F='OctetString'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='POLICY-FRAMEWORK-PIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
policy,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','policy')
policyFrameworkPib=ModuleIdentity((1,3,6,1,4,1,45,4,1))
if mibBuilder.loadTexts:policyFrameworkPib.setRevisions(('2004-07-20 00:00',))
class Role(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class RoleCombination(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PolicyInstanceId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PolicyBasePibClass_ObjectIdentity=ObjectIdentity
policyBasePibClass=_PolicyBasePibClass_ObjectIdentity((1,3,6,1,4,1,45,4,1,1))
_PolicyPrcSupportTable_Object=MibTable
policyPrcSupportTable=_PolicyPrcSupportTable_Object((1,3,6,1,4,1,45,4,1,1,1))
if mibBuilder.loadTexts:policyPrcSupportTable.setStatus(_A)
_PolicyPrcSupportEntry_Object=MibTableRow
policyPrcSupportEntry=_PolicyPrcSupportEntry_Object((1,3,6,1,4,1,45,4,1,1,1,1))
policyPrcSupportEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:policyPrcSupportEntry.setStatus(_A)
_PolicyPrcSupportPrid_Type=PolicyInstanceId
_PolicyPrcSupportPrid_Object=MibTableColumn
policyPrcSupportPrid=_PolicyPrcSupportPrid_Object((1,3,6,1,4,1,45,4,1,1,1,1,1),_PolicyPrcSupportPrid_Type())
policyPrcSupportPrid.setMaxAccess(_E)
if mibBuilder.loadTexts:policyPrcSupportPrid.setStatus(_A)
_PolicyPrcSupportSupportedPrc_Type=ObjectIdentifier
_PolicyPrcSupportSupportedPrc_Object=MibTableColumn
policyPrcSupportSupportedPrc=_PolicyPrcSupportSupportedPrc_Object((1,3,6,1,4,1,45,4,1,1,1,1,2),_PolicyPrcSupportSupportedPrc_Type())
policyPrcSupportSupportedPrc.setMaxAccess(_C)
if mibBuilder.loadTexts:policyPrcSupportSupportedPrc.setStatus(_A)
_PolicyPrcSupportSupportedAttrs_Type=OctetString
_PolicyPrcSupportSupportedAttrs_Object=MibTableColumn
policyPrcSupportSupportedAttrs=_PolicyPrcSupportSupportedAttrs_Object((1,3,6,1,4,1,45,4,1,1,1,1,3),_PolicyPrcSupportSupportedAttrs_Type())
policyPrcSupportSupportedAttrs.setMaxAccess(_C)
if mibBuilder.loadTexts:policyPrcSupportSupportedAttrs.setStatus(_A)
_PolicyPrcSupportMaxPris_Type=Unsigned32
_PolicyPrcSupportMaxPris_Object=MibTableColumn
policyPrcSupportMaxPris=_PolicyPrcSupportMaxPris_Object((1,3,6,1,4,1,45,4,1,1,1,1,4),_PolicyPrcSupportMaxPris_Type())
policyPrcSupportMaxPris.setMaxAccess(_C)
if mibBuilder.loadTexts:policyPrcSupportMaxPris.setStatus(_A)
_PolicyPibIncarnationTable_Object=MibTable
policyPibIncarnationTable=_PolicyPibIncarnationTable_Object((1,3,6,1,4,1,45,4,1,1,2))
if mibBuilder.loadTexts:policyPibIncarnationTable.setStatus(_A)
_PolicyPibIncarnationEntry_Object=MibTableRow
policyPibIncarnationEntry=_PolicyPibIncarnationEntry_Object((1,3,6,1,4,1,45,4,1,1,2,1))
policyPibIncarnationEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:policyPibIncarnationEntry.setStatus(_A)
_PolicyPibIncarnationPrid_Type=PolicyInstanceId
_PolicyPibIncarnationPrid_Object=MibTableColumn
policyPibIncarnationPrid=_PolicyPibIncarnationPrid_Object((1,3,6,1,4,1,45,4,1,1,2,1,1),_PolicyPibIncarnationPrid_Type())
policyPibIncarnationPrid.setMaxAccess(_E)
if mibBuilder.loadTexts:policyPibIncarnationPrid.setStatus(_A)
_PolicyPibIncarnationName_Type=SnmpAdminString
_PolicyPibIncarnationName_Object=MibTableColumn
policyPibIncarnationName=_PolicyPibIncarnationName_Object((1,3,6,1,4,1,45,4,1,1,2,1,2),_PolicyPibIncarnationName_Type())
policyPibIncarnationName.setMaxAccess(_D)
if mibBuilder.loadTexts:policyPibIncarnationName.setStatus(_A)
_PolicyPibIncarnationId_Type=OctetString
_PolicyPibIncarnationId_Object=MibTableColumn
policyPibIncarnationId=_PolicyPibIncarnationId_Object((1,3,6,1,4,1,45,4,1,1,2,1,3),_PolicyPibIncarnationId_Type())
policyPibIncarnationId.setMaxAccess(_D)
if mibBuilder.loadTexts:policyPibIncarnationId.setStatus(_A)
class _PolicyPibIncarnationLongevity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('expireNever',1),('expireImmediate',2),('expireOnTimeout',3)))
_PolicyPibIncarnationLongevity_Type.__name__=_H
_PolicyPibIncarnationLongevity_Object=MibTableColumn
policyPibIncarnationLongevity=_PolicyPibIncarnationLongevity_Object((1,3,6,1,4,1,45,4,1,1,2,1,4),_PolicyPibIncarnationLongevity_Type())
policyPibIncarnationLongevity.setMaxAccess(_D)
if mibBuilder.loadTexts:policyPibIncarnationLongevity.setStatus(_A)
_PolicyPibIncarnationTtl_Type=Unsigned32
_PolicyPibIncarnationTtl_Object=MibTableColumn
policyPibIncarnationTtl=_PolicyPibIncarnationTtl_Object((1,3,6,1,4,1,45,4,1,1,2,1,5),_PolicyPibIncarnationTtl_Type())
policyPibIncarnationTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:policyPibIncarnationTtl.setStatus(_A)
_PolicyPibIncarnationActive_Type=TruthValue
_PolicyPibIncarnationActive_Object=MibTableColumn
policyPibIncarnationActive=_PolicyPibIncarnationActive_Object((1,3,6,1,4,1,45,4,1,1,2,1,6),_PolicyPibIncarnationActive_Type())
policyPibIncarnationActive.setMaxAccess(_D)
if mibBuilder.loadTexts:policyPibIncarnationActive.setStatus(_A)
_PolicyDeviceIdentificationTable_Object=MibTable
policyDeviceIdentificationTable=_PolicyDeviceIdentificationTable_Object((1,3,6,1,4,1,45,4,1,1,3))
if mibBuilder.loadTexts:policyDeviceIdentificationTable.setStatus(_A)
_PolicyDeviceIdentificationEntry_Object=MibTableRow
policyDeviceIdentificationEntry=_PolicyDeviceIdentificationEntry_Object((1,3,6,1,4,1,45,4,1,1,3,1))
policyDeviceIdentificationEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:policyDeviceIdentificationEntry.setStatus(_A)
_PolicyDeviceIdentificationPrid_Type=PolicyInstanceId
_PolicyDeviceIdentificationPrid_Object=MibTableColumn
policyDeviceIdentificationPrid=_PolicyDeviceIdentificationPrid_Object((1,3,6,1,4,1,45,4,1,1,3,1,1),_PolicyDeviceIdentificationPrid_Type())
policyDeviceIdentificationPrid.setMaxAccess(_E)
if mibBuilder.loadTexts:policyDeviceIdentificationPrid.setStatus(_A)
class _PolicyDeviceIdentificationDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PolicyDeviceIdentificationDescr_Type.__name__=_G
_PolicyDeviceIdentificationDescr_Object=MibTableColumn
policyDeviceIdentificationDescr=_PolicyDeviceIdentificationDescr_Object((1,3,6,1,4,1,45,4,1,1,3,1,2),_PolicyDeviceIdentificationDescr_Type())
policyDeviceIdentificationDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:policyDeviceIdentificationDescr.setStatus(_A)
_PolicyDeviceIdentificationMaxMsg_Type=Unsigned32
_PolicyDeviceIdentificationMaxMsg_Object=MibTableColumn
policyDeviceIdentificationMaxMsg=_PolicyDeviceIdentificationMaxMsg_Object((1,3,6,1,4,1,45,4,1,1,3,1,3),_PolicyDeviceIdentificationMaxMsg_Type())
policyDeviceIdentificationMaxMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:policyDeviceIdentificationMaxMsg.setStatus(_A)
_PolicyCompLimitsTable_Object=MibTable
policyCompLimitsTable=_PolicyCompLimitsTable_Object((1,3,6,1,4,1,45,4,1,1,4))
if mibBuilder.loadTexts:policyCompLimitsTable.setStatus(_A)
_PolicyCompLimitsEntry_Object=MibTableRow
policyCompLimitsEntry=_PolicyCompLimitsEntry_Object((1,3,6,1,4,1,45,4,1,1,4,1))
policyCompLimitsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:policyCompLimitsEntry.setStatus(_A)
_PolicyCompLimitsPrid_Type=PolicyInstanceId
_PolicyCompLimitsPrid_Object=MibTableColumn
policyCompLimitsPrid=_PolicyCompLimitsPrid_Object((1,3,6,1,4,1,45,4,1,1,4,1,1),_PolicyCompLimitsPrid_Type())
policyCompLimitsPrid.setMaxAccess(_E)
if mibBuilder.loadTexts:policyCompLimitsPrid.setStatus(_A)
_PolicyCompLimitsComponent_Type=ObjectIdentifier
_PolicyCompLimitsComponent_Object=MibTableColumn
policyCompLimitsComponent=_PolicyCompLimitsComponent_Object((1,3,6,1,4,1,45,4,1,1,4,1,2),_PolicyCompLimitsComponent_Type())
policyCompLimitsComponent.setMaxAccess(_C)
if mibBuilder.loadTexts:policyCompLimitsComponent.setStatus(_A)
_PolicyCompLimitsType_Type=Integer32
_PolicyCompLimitsType_Object=MibTableColumn
policyCompLimitsType=_PolicyCompLimitsType_Object((1,3,6,1,4,1,45,4,1,1,4,1,3),_PolicyCompLimitsType_Type())
policyCompLimitsType.setMaxAccess(_C)
if mibBuilder.loadTexts:policyCompLimitsType.setStatus(_A)
class _PolicyCompLimitsGuidance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PolicyCompLimitsGuidance_Type.__name__=_F
_PolicyCompLimitsGuidance_Object=MibTableColumn
policyCompLimitsGuidance=_PolicyCompLimitsGuidance_Object((1,3,6,1,4,1,45,4,1,1,4,1,4),_PolicyCompLimitsGuidance_Type())
policyCompLimitsGuidance.setMaxAccess(_C)
if mibBuilder.loadTexts:policyCompLimitsGuidance.setStatus(_A)
_PolicyBasePibConformance_ObjectIdentity=ObjectIdentity
policyBasePibConformance=_PolicyBasePibConformance_ObjectIdentity((1,3,6,1,4,1,45,4,1,2))
_PolicyBasePibCompliances_ObjectIdentity=ObjectIdentity
policyBasePibCompliances=_PolicyBasePibCompliances_ObjectIdentity((1,3,6,1,4,1,45,4,1,2,1))
_PolicyBasePibGroups_ObjectIdentity=ObjectIdentity
policyBasePibGroups=_PolicyBasePibGroups_ObjectIdentity((1,3,6,1,4,1,45,4,1,2,2))
policyPrcSupportGroup=ObjectGroup((1,3,6,1,4,1,45,4,1,2,2,1))
policyPrcSupportGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:policyPrcSupportGroup.setStatus(_A)
policyPibIncarnationGroup=ObjectGroup((1,3,6,1,4,1,45,4,1,2,2,2))
policyPibIncarnationGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:policyPibIncarnationGroup.setStatus(_A)
policyDeviceIdentificationGroup=ObjectGroup((1,3,6,1,4,1,45,4,1,2,2,3))
policyDeviceIdentificationGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:policyDeviceIdentificationGroup.setStatus(_A)
policyCompLimitsGroup=ObjectGroup((1,3,6,1,4,1,45,4,1,2,2,4))
policyCompLimitsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:policyCompLimitsGroup.setStatus(_A)
policyBasePibCompliance=ModuleCompliance((1,3,6,1,4,1,45,4,1,2,1,1))
policyBasePibCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:policyBasePibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Role':Role,'RoleCombination':RoleCombination,'PolicyInstanceId':PolicyInstanceId,'policyFrameworkPib':policyFrameworkPib,'policyBasePibClass':policyBasePibClass,'policyPrcSupportTable':policyPrcSupportTable,'policyPrcSupportEntry':policyPrcSupportEntry,_I:policyPrcSupportPrid,_M:policyPrcSupportSupportedPrc,_N:policyPrcSupportSupportedAttrs,_O:policyPrcSupportMaxPris,'policyPibIncarnationTable':policyPibIncarnationTable,'policyPibIncarnationEntry':policyPibIncarnationEntry,_J:policyPibIncarnationPrid,_P:policyPibIncarnationName,_Q:policyPibIncarnationId,_R:policyPibIncarnationLongevity,_S:policyPibIncarnationTtl,_T:policyPibIncarnationActive,'policyDeviceIdentificationTable':policyDeviceIdentificationTable,'policyDeviceIdentificationEntry':policyDeviceIdentificationEntry,_K:policyDeviceIdentificationPrid,_U:policyDeviceIdentificationDescr,_V:policyDeviceIdentificationMaxMsg,'policyCompLimitsTable':policyCompLimitsTable,'policyCompLimitsEntry':policyCompLimitsEntry,_L:policyCompLimitsPrid,_W:policyCompLimitsComponent,_X:policyCompLimitsType,_Y:policyCompLimitsGuidance,'policyBasePibConformance':policyBasePibConformance,'policyBasePibCompliances':policyBasePibCompliances,'policyBasePibCompliance':policyBasePibCompliance,'policyBasePibGroups':policyBasePibGroups,_Z:policyPrcSupportGroup,_a:policyPibIncarnationGroup,_b:policyDeviceIdentificationGroup,_c:policyCompLimitsGroup})