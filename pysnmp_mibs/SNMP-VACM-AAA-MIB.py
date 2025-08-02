_J='vacmAaaGroup'
_I='vacmAaaGroupName'
_H='vacmAaaSessionID'
_G='vacmAaaSecurityName'
_F='vacmAaaSecurityModel'
_E='SnmpSecurityModel'
_D='not-accessible'
_C='SnmpAdminString'
_B='SNMP-VACM-AAA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,SnmpSecurityModel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vacmAaaMIB=ModuleIdentity((1,3,6,1,2,1,199))
if mibBuilder.loadTexts:vacmAaaMIB.setRevisions(('2010-12-09 00:00',))
_VacmAaaMIBObjects_ObjectIdentity=ObjectIdentity
vacmAaaMIBObjects=_VacmAaaMIBObjects_ObjectIdentity((1,3,6,1,2,1,199,1))
_VacmAaaSecurityToGroupTable_Object=MibTable
vacmAaaSecurityToGroupTable=_VacmAaaSecurityToGroupTable_Object((1,3,6,1,2,1,199,1,1))
if mibBuilder.loadTexts:vacmAaaSecurityToGroupTable.setStatus(_A)
_VacmAaaSecurityToGroupEntry_Object=MibTableRow
vacmAaaSecurityToGroupEntry=_VacmAaaSecurityToGroupEntry_Object((1,3,6,1,2,1,199,1,1,1))
vacmAaaSecurityToGroupEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:vacmAaaSecurityToGroupEntry.setStatus(_A)
class _VacmAaaSecurityModel_Type(SnmpSecurityModel):subtypeSpec=SnmpSecurityModel.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VacmAaaSecurityModel_Type.__name__=_E
_VacmAaaSecurityModel_Object=MibTableColumn
vacmAaaSecurityModel=_VacmAaaSecurityModel_Object((1,3,6,1,2,1,199,1,1,1,1),_VacmAaaSecurityModel_Type())
vacmAaaSecurityModel.setMaxAccess(_D)
if mibBuilder.loadTexts:vacmAaaSecurityModel.setStatus(_A)
class _VacmAaaSecurityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_VacmAaaSecurityName_Type.__name__=_C
_VacmAaaSecurityName_Object=MibTableColumn
vacmAaaSecurityName=_VacmAaaSecurityName_Object((1,3,6,1,2,1,199,1,1,1,2),_VacmAaaSecurityName_Type())
vacmAaaSecurityName.setMaxAccess(_D)
if mibBuilder.loadTexts:vacmAaaSecurityName.setStatus(_A)
_VacmAaaSessionID_Type=Unsigned32
_VacmAaaSessionID_Object=MibTableColumn
vacmAaaSessionID=_VacmAaaSessionID_Object((1,3,6,1,2,1,199,1,1,1,3),_VacmAaaSessionID_Type())
vacmAaaSessionID.setMaxAccess(_D)
if mibBuilder.loadTexts:vacmAaaSessionID.setStatus(_A)
class _VacmAaaGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_VacmAaaGroupName_Type.__name__=_C
_VacmAaaGroupName_Object=MibTableColumn
vacmAaaGroupName=_VacmAaaGroupName_Object((1,3,6,1,2,1,199,1,1,1,4),_VacmAaaGroupName_Type())
vacmAaaGroupName.setMaxAccess('read-only')
if mibBuilder.loadTexts:vacmAaaGroupName.setStatus(_A)
_VacmAaaMIBConformance_ObjectIdentity=ObjectIdentity
vacmAaaMIBConformance=_VacmAaaMIBConformance_ObjectIdentity((1,3,6,1,2,1,199,2))
_VacmAaaMIBCompliances_ObjectIdentity=ObjectIdentity
vacmAaaMIBCompliances=_VacmAaaMIBCompliances_ObjectIdentity((1,3,6,1,2,1,199,2,1))
_VacmAaaMIBGroups_ObjectIdentity=ObjectIdentity
vacmAaaMIBGroups=_VacmAaaMIBGroups_ObjectIdentity((1,3,6,1,2,1,199,2,2))
vacmAaaGroup=ObjectGroup((1,3,6,1,2,1,199,2,2,1))
vacmAaaGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:vacmAaaGroup.setStatus(_A)
vacmAaaMIBBasicCompliance=ModuleCompliance((1,3,6,1,2,1,199,2,1,1))
vacmAaaMIBBasicCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:vacmAaaMIBBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vacmAaaMIB':vacmAaaMIB,'vacmAaaMIBObjects':vacmAaaMIBObjects,'vacmAaaSecurityToGroupTable':vacmAaaSecurityToGroupTable,'vacmAaaSecurityToGroupEntry':vacmAaaSecurityToGroupEntry,_F:vacmAaaSecurityModel,_G:vacmAaaSecurityName,_H:vacmAaaSessionID,_I:vacmAaaGroupName,'vacmAaaMIBConformance':vacmAaaMIBConformance,'vacmAaaMIBCompliances':vacmAaaMIBCompliances,'vacmAaaMIBBasicCompliance':vacmAaaMIBBasicCompliance,'vacmAaaMIBGroups':vacmAaaMIBGroups,_J:vacmAaaGroup})