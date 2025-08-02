_I='oaSnmpSecurStrGroup'
_H='oaSnmpSecurStrAdminStatus'
_G='oaSnmpSecurStrAccessPermission'
_F='read-write'
_E='oaSnmpSecurStrName'
_D='DisplayString'
_C='Integer32'
_B='OA-PROTOCOL-PARAMETERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
oaProtocolParams=ModuleIdentity((1,3,6,1,4,1,6926,1,42))
if mibBuilder.loadTexts:oaProtocolParams.setRevisions(('2008-11-24 00:00',))
class EntryValidator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('nothing',2),('delete',3),('create',4),('enable',5),('disable',6)))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaSnmpPrtcl_ObjectIdentity=ObjectIdentity
oaSnmpPrtcl=_OaSnmpPrtcl_ObjectIdentity((1,3,6,1,4,1,6926,1,42,2))
_OaSnmpSecurStrTable_Object=MibTable
oaSnmpSecurStrTable=_OaSnmpSecurStrTable_Object((1,3,6,1,4,1,6926,1,42,2,2))
if mibBuilder.loadTexts:oaSnmpSecurStrTable.setStatus(_A)
_OaSnmpSecurStrEntry_Object=MibTableRow
oaSnmpSecurStrEntry=_OaSnmpSecurStrEntry_Object((1,3,6,1,4,1,6926,1,42,2,2,1))
oaSnmpSecurStrEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:oaSnmpSecurStrEntry.setStatus(_A)
class _OaSnmpSecurStrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_OaSnmpSecurStrName_Type.__name__=_D
_OaSnmpSecurStrName_Object=MibTableColumn
oaSnmpSecurStrName=_OaSnmpSecurStrName_Object((1,3,6,1,4,1,6926,1,42,2,2,1,1),_OaSnmpSecurStrName_Type())
oaSnmpSecurStrName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oaSnmpSecurStrName.setStatus(_A)
class _OaSnmpSecurStrAccessPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_OaSnmpSecurStrAccessPermission_Type.__name__=_C
_OaSnmpSecurStrAccessPermission_Object=MibTableColumn
oaSnmpSecurStrAccessPermission=_OaSnmpSecurStrAccessPermission_Object((1,3,6,1,4,1,6926,1,42,2,2,1,2),_OaSnmpSecurStrAccessPermission_Type())
oaSnmpSecurStrAccessPermission.setMaxAccess(_F)
if mibBuilder.loadTexts:oaSnmpSecurStrAccessPermission.setStatus(_A)
_OaSnmpSecurStrAdminStatus_Type=EntryValidator
_OaSnmpSecurStrAdminStatus_Object=MibTableColumn
oaSnmpSecurStrAdminStatus=_OaSnmpSecurStrAdminStatus_Object((1,3,6,1,4,1,6926,1,42,2,2,1,11),_OaSnmpSecurStrAdminStatus_Type())
oaSnmpSecurStrAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:oaSnmpSecurStrAdminStatus.setStatus(_A)
_OaPrtclConformance_ObjectIdentity=ObjectIdentity
oaPrtclConformance=_OaPrtclConformance_ObjectIdentity((1,3,6,1,4,1,6926,1,42,101))
_OaPrtclMIBCompliances_ObjectIdentity=ObjectIdentity
oaPrtclMIBCompliances=_OaPrtclMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,1,42,101,1))
_OaPrtclMIBGroups_ObjectIdentity=ObjectIdentity
oaPrtclMIBGroups=_OaPrtclMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,1,42,101,2))
oaSnmpSecurStrGroup=ObjectGroup((1,3,6,1,4,1,6926,1,42,101,2,1))
oaSnmpSecurStrGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:oaSnmpSecurStrGroup.setStatus(_A)
oaPrtclMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,1,42,101,1,1))
oaPrtclMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:oaPrtclMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EntryValidator':EntryValidator,'oaccess':oaccess,'oaManagement':oaManagement,'oaProtocolParams':oaProtocolParams,'oaSnmpPrtcl':oaSnmpPrtcl,'oaSnmpSecurStrTable':oaSnmpSecurStrTable,'oaSnmpSecurStrEntry':oaSnmpSecurStrEntry,_E:oaSnmpSecurStrName,_G:oaSnmpSecurStrAccessPermission,_H:oaSnmpSecurStrAdminStatus,'oaPrtclConformance':oaPrtclConformance,'oaPrtclMIBCompliances':oaPrtclMIBCompliances,'oaPrtclMIBCompliance':oaPrtclMIBCompliance,'oaPrtclMIBGroups':oaPrtclMIBGroups,_I:oaSnmpSecurStrGroup})