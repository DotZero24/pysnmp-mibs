_R='usmDHKeyKickstartGroup'
_Q='usmDHKeyParamGroup'
_P='usmDHKeyMIBBasicGroup'
_O='usmDHKickstartSecurityName'
_N='usmDHKickstartMgrPublic'
_M='usmDHKickstartMyPublic'
_L='usmDHParameters'
_K='usmDHUserOwnPrivKeyChange'
_J='usmDHUserPrivKeyChange'
_I='usmDHUserOwnAuthKeyChange'
_H='usmDHUserAuthKeyChange'
_G='usmDHUserKeyEntry'
_F='usmDHKickstartIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='SNMP-USM-DH-OBJECTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
usmUserEntry,=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB','usmUserEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpUsmDHObjectsMIB=ModuleIdentity((1,3,6,1,3,101))
if mibBuilder.loadTexts:snmpUsmDHObjectsMIB.setRevisions(('2000-03-06 00:00',))
class DHKeyChange(TextualConvention,OctetString):status=_A
_UsmDHKeyObjects_ObjectIdentity=ObjectIdentity
usmDHKeyObjects=_UsmDHKeyObjects_ObjectIdentity((1,3,6,1,3,101,1))
_UsmDHPublicObjects_ObjectIdentity=ObjectIdentity
usmDHPublicObjects=_UsmDHPublicObjects_ObjectIdentity((1,3,6,1,3,101,1,1))
_UsmDHParameters_Type=OctetString
_UsmDHParameters_Object=MibScalar
usmDHParameters=_UsmDHParameters_Object((1,3,6,1,3,101,1,1,1),_UsmDHParameters_Type())
usmDHParameters.setMaxAccess('read-write')
if mibBuilder.loadTexts:usmDHParameters.setStatus(_A)
_UsmDHUserKeyTable_Object=MibTable
usmDHUserKeyTable=_UsmDHUserKeyTable_Object((1,3,6,1,3,101,1,1,2))
if mibBuilder.loadTexts:usmDHUserKeyTable.setStatus(_A)
_UsmDHUserKeyEntry_Object=MibTableRow
usmDHUserKeyEntry=_UsmDHUserKeyEntry_Object((1,3,6,1,3,101,1,1,2,1))
if mibBuilder.loadTexts:usmDHUserKeyEntry.setStatus(_A)
_UsmDHUserAuthKeyChange_Type=DHKeyChange
_UsmDHUserAuthKeyChange_Object=MibTableColumn
usmDHUserAuthKeyChange=_UsmDHUserAuthKeyChange_Object((1,3,6,1,3,101,1,1,2,1,1),_UsmDHUserAuthKeyChange_Type())
usmDHUserAuthKeyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:usmDHUserAuthKeyChange.setStatus(_A)
_UsmDHUserOwnAuthKeyChange_Type=DHKeyChange
_UsmDHUserOwnAuthKeyChange_Object=MibTableColumn
usmDHUserOwnAuthKeyChange=_UsmDHUserOwnAuthKeyChange_Object((1,3,6,1,3,101,1,1,2,1,2),_UsmDHUserOwnAuthKeyChange_Type())
usmDHUserOwnAuthKeyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:usmDHUserOwnAuthKeyChange.setStatus(_A)
_UsmDHUserPrivKeyChange_Type=DHKeyChange
_UsmDHUserPrivKeyChange_Object=MibTableColumn
usmDHUserPrivKeyChange=_UsmDHUserPrivKeyChange_Object((1,3,6,1,3,101,1,1,2,1,3),_UsmDHUserPrivKeyChange_Type())
usmDHUserPrivKeyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:usmDHUserPrivKeyChange.setStatus(_A)
_UsmDHUserOwnPrivKeyChange_Type=DHKeyChange
_UsmDHUserOwnPrivKeyChange_Object=MibTableColumn
usmDHUserOwnPrivKeyChange=_UsmDHUserOwnPrivKeyChange_Object((1,3,6,1,3,101,1,1,2,1,4),_UsmDHUserOwnPrivKeyChange_Type())
usmDHUserOwnPrivKeyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:usmDHUserOwnPrivKeyChange.setStatus(_A)
_UsmDHKickstartGroup_ObjectIdentity=ObjectIdentity
usmDHKickstartGroup=_UsmDHKickstartGroup_ObjectIdentity((1,3,6,1,3,101,1,2))
_UsmDHKickstartTable_Object=MibTable
usmDHKickstartTable=_UsmDHKickstartTable_Object((1,3,6,1,3,101,1,2,1))
if mibBuilder.loadTexts:usmDHKickstartTable.setStatus(_A)
_UsmDHKickstartEntry_Object=MibTableRow
usmDHKickstartEntry=_UsmDHKickstartEntry_Object((1,3,6,1,3,101,1,2,1,1))
usmDHKickstartEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:usmDHKickstartEntry.setStatus(_A)
class _UsmDHKickstartIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_UsmDHKickstartIndex_Type.__name__=_E
_UsmDHKickstartIndex_Object=MibTableColumn
usmDHKickstartIndex=_UsmDHKickstartIndex_Object((1,3,6,1,3,101,1,2,1,1,1),_UsmDHKickstartIndex_Type())
usmDHKickstartIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:usmDHKickstartIndex.setStatus(_A)
_UsmDHKickstartMyPublic_Type=OctetString
_UsmDHKickstartMyPublic_Object=MibTableColumn
usmDHKickstartMyPublic=_UsmDHKickstartMyPublic_Object((1,3,6,1,3,101,1,2,1,1,2),_UsmDHKickstartMyPublic_Type())
usmDHKickstartMyPublic.setMaxAccess(_D)
if mibBuilder.loadTexts:usmDHKickstartMyPublic.setStatus(_A)
_UsmDHKickstartMgrPublic_Type=OctetString
_UsmDHKickstartMgrPublic_Object=MibTableColumn
usmDHKickstartMgrPublic=_UsmDHKickstartMgrPublic_Object((1,3,6,1,3,101,1,2,1,1,3),_UsmDHKickstartMgrPublic_Type())
usmDHKickstartMgrPublic.setMaxAccess(_D)
if mibBuilder.loadTexts:usmDHKickstartMgrPublic.setStatus(_A)
_UsmDHKickstartSecurityName_Type=SnmpAdminString
_UsmDHKickstartSecurityName_Object=MibTableColumn
usmDHKickstartSecurityName=_UsmDHKickstartSecurityName_Object((1,3,6,1,3,101,1,2,1,1,4),_UsmDHKickstartSecurityName_Type())
usmDHKickstartSecurityName.setMaxAccess(_D)
if mibBuilder.loadTexts:usmDHKickstartSecurityName.setStatus(_A)
_UsmDHKeyConformance_ObjectIdentity=ObjectIdentity
usmDHKeyConformance=_UsmDHKeyConformance_ObjectIdentity((1,3,6,1,3,101,2))
_UsmDHKeyMIBCompliances_ObjectIdentity=ObjectIdentity
usmDHKeyMIBCompliances=_UsmDHKeyMIBCompliances_ObjectIdentity((1,3,6,1,3,101,2,1))
_UsmDHKeyMIBGroups_ObjectIdentity=ObjectIdentity
usmDHKeyMIBGroups=_UsmDHKeyMIBGroups_ObjectIdentity((1,3,6,1,3,101,2,2))
usmUserEntry.registerAugmentions((_B,_G))
usmDHUserKeyEntry.setIndexNames(*usmUserEntry.getIndexNames())
usmDHKeyMIBBasicGroup=ObjectGroup((1,3,6,1,3,101,2,2,1))
usmDHKeyMIBBasicGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:usmDHKeyMIBBasicGroup.setStatus(_A)
usmDHKeyParamGroup=ObjectGroup((1,3,6,1,3,101,2,2,2))
usmDHKeyParamGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:usmDHKeyParamGroup.setStatus(_A)
usmDHKeyKickstartGroup=ObjectGroup((1,3,6,1,3,101,2,2,3))
usmDHKeyKickstartGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:usmDHKeyKickstartGroup.setStatus(_A)
usmDHKeyMIBCompliance=ModuleCompliance((1,3,6,1,3,101,2,1,1))
usmDHKeyMIBCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:usmDHKeyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DHKeyChange':DHKeyChange,'snmpUsmDHObjectsMIB':snmpUsmDHObjectsMIB,'usmDHKeyObjects':usmDHKeyObjects,'usmDHPublicObjects':usmDHPublicObjects,_L:usmDHParameters,'usmDHUserKeyTable':usmDHUserKeyTable,_G:usmDHUserKeyEntry,_H:usmDHUserAuthKeyChange,_I:usmDHUserOwnAuthKeyChange,_J:usmDHUserPrivKeyChange,_K:usmDHUserOwnPrivKeyChange,'usmDHKickstartGroup':usmDHKickstartGroup,'usmDHKickstartTable':usmDHKickstartTable,'usmDHKickstartEntry':usmDHKickstartEntry,_F:usmDHKickstartIndex,_M:usmDHKickstartMyPublic,_N:usmDHKickstartMgrPublic,_O:usmDHKickstartSecurityName,'usmDHKeyConformance':usmDHKeyConformance,'usmDHKeyMIBCompliances':usmDHKeyMIBCompliances,'usmDHKeyMIBCompliance':usmDHKeyMIBCompliance,'usmDHKeyMIBGroups':usmDHKeyMIBGroups,_P:usmDHKeyMIBBasicGroup,_Q:usmDHKeyParamGroup,_R:usmDHKeyKickstartGroup})