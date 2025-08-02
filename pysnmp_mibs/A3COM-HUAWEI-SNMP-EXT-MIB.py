_L='h3cSnmpCommunityExName'
_K='not-accessible'
_J='h3cSnmpExtCommunitySecurityName'
_I='h3cSnmpExtCommunitySecurityLevel'
_H='TruthValue'
_G='SnmpAdminString'
_F='A3COM-HUAWEI-SNMP-EXT-MIB'
_E='read-write'
_D='Integer32'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
SnmpAdminString,SnmpSecurityLevel,SnmpSecurityModel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G,'SnmpSecurityLevel','SnmpSecurityModel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
h3cSnmpExt=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,104))
if mibBuilder.loadTexts:h3cSnmpExt.setRevisions(('2009-04-07 17:00',))
_H3cSnmpExtScalarObjects_ObjectIdentity=ObjectIdentity
h3cSnmpExtScalarObjects=_H3cSnmpExtScalarObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,104,1))
class _H3cSnmpExtSnmpChannel_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSnmpExtSnmpChannel_Type.__name__=_D
_H3cSnmpExtSnmpChannel_Object=MibScalar
h3cSnmpExtSnmpChannel=_H3cSnmpExtSnmpChannel_Object((1,3,6,1,4,1,43,45,1,10,2,104,1,1),_H3cSnmpExtSnmpChannel_Type())
h3cSnmpExtSnmpChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtSnmpChannel.setStatus(_A)
class _H3cSnmpExtReadCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtReadCommunitySingle_Type.__name__=_G
_H3cSnmpExtReadCommunitySingle_Object=MibScalar
h3cSnmpExtReadCommunitySingle=_H3cSnmpExtReadCommunitySingle_Object((1,3,6,1,4,1,43,45,1,10,2,104,1,2),_H3cSnmpExtReadCommunitySingle_Type())
h3cSnmpExtReadCommunitySingle.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtReadCommunitySingle.setStatus(_A)
class _H3cSnmpExtWriteCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtWriteCommunitySingle_Type.__name__=_G
_H3cSnmpExtWriteCommunitySingle_Object=MibScalar
h3cSnmpExtWriteCommunitySingle=_H3cSnmpExtWriteCommunitySingle_Object((1,3,6,1,4,1,43,45,1,10,2,104,1,3),_H3cSnmpExtWriteCommunitySingle_Type())
h3cSnmpExtWriteCommunitySingle.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtWriteCommunitySingle.setStatus(_A)
_H3cSnmpExtTables_ObjectIdentity=ObjectIdentity
h3cSnmpExtTables=_H3cSnmpExtTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,104,2))
_H3cSnmpExtCommunityTable_Object=MibTable
h3cSnmpExtCommunityTable=_H3cSnmpExtCommunityTable_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1))
if mibBuilder.loadTexts:h3cSnmpExtCommunityTable.setStatus(_A)
_H3cSnmpExtCommunityEntry_Object=MibTableRow
h3cSnmpExtCommunityEntry=_H3cSnmpExtCommunityEntry_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1,1))
h3cSnmpExtCommunityEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:h3cSnmpExtCommunityEntry.setStatus(_A)
_H3cSnmpExtCommunitySecurityLevel_Type=SnmpSecurityModel
_H3cSnmpExtCommunitySecurityLevel_Object=MibTableColumn
h3cSnmpExtCommunitySecurityLevel=_H3cSnmpExtCommunitySecurityLevel_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1,1,1),_H3cSnmpExtCommunitySecurityLevel_Type())
h3cSnmpExtCommunitySecurityLevel.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSnmpExtCommunitySecurityLevel.setStatus(_A)
_H3cSnmpExtCommunitySecurityName_Type=SnmpAdminString
_H3cSnmpExtCommunitySecurityName_Object=MibTableColumn
h3cSnmpExtCommunitySecurityName=_H3cSnmpExtCommunitySecurityName_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1,1,2),_H3cSnmpExtCommunitySecurityName_Type())
h3cSnmpExtCommunitySecurityName.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSnmpExtCommunitySecurityName.setStatus(_A)
class _H3cSnmpExtCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtCommunityName_Type.__name__=_C
_H3cSnmpExtCommunityName_Object=MibTableColumn
h3cSnmpExtCommunityName=_H3cSnmpExtCommunityName_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1,1,3),_H3cSnmpExtCommunityName_Type())
h3cSnmpExtCommunityName.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cSnmpExtCommunityName.setStatus(_A)
class _H3cSnmpExtCommunityAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_H3cSnmpExtCommunityAclNum_Type.__name__=_D
_H3cSnmpExtCommunityAclNum_Object=MibTableColumn
h3cSnmpExtCommunityAclNum=_H3cSnmpExtCommunityAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,1,1,4),_H3cSnmpExtCommunityAclNum_Type())
h3cSnmpExtCommunityAclNum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtCommunityAclNum.setStatus(_A)
_H3cSnmpCommunityExTable_Object=MibTable
h3cSnmpCommunityExTable=_H3cSnmpCommunityExTable_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2))
if mibBuilder.loadTexts:h3cSnmpCommunityExTable.setStatus(_A)
_H3cSnmpCommunityExEntry_Object=MibTableRow
h3cSnmpCommunityExEntry=_H3cSnmpCommunityExEntry_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1))
h3cSnmpCommunityExEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:h3cSnmpCommunityExEntry.setStatus(_A)
class _H3cSnmpCommunityExName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpCommunityExName_Type.__name__=_C
_H3cSnmpCommunityExName_Object=MibTableColumn
h3cSnmpCommunityExName=_H3cSnmpCommunityExName_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1,1),_H3cSnmpCommunityExName_Type())
h3cSnmpCommunityExName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnmpCommunityExName.setStatus(_A)
class _H3cSnmpCommunityExWrite_Type(TruthValue):defaultValue=2
_H3cSnmpCommunityExWrite_Type.__name__=_H
_H3cSnmpCommunityExWrite_Object=MibTableColumn
h3cSnmpCommunityExWrite=_H3cSnmpCommunityExWrite_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1,2),_H3cSnmpCommunityExWrite_Type())
h3cSnmpCommunityExWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnmpCommunityExWrite.setStatus(_A)
class _H3cSnmpCommunityExViewName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpCommunityExViewName_Type.__name__=_C
_H3cSnmpCommunityExViewName_Object=MibTableColumn
h3cSnmpCommunityExViewName=_H3cSnmpCommunityExViewName_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1,3),_H3cSnmpCommunityExViewName_Type())
h3cSnmpCommunityExViewName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnmpCommunityExViewName.setStatus(_A)
class _H3cSnmpCommunityExAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_H3cSnmpCommunityExAclNum_Type.__name__=_D
_H3cSnmpCommunityExAclNum_Object=MibTableColumn
h3cSnmpCommunityExAclNum=_H3cSnmpCommunityExAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1,4),_H3cSnmpCommunityExAclNum_Type())
h3cSnmpCommunityExAclNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnmpCommunityExAclNum.setStatus(_A)
_H3cSnmpCommunityExRowStatus_Type=RowStatus
_H3cSnmpCommunityExRowStatus_Object=MibTableColumn
h3cSnmpCommunityExRowStatus=_H3cSnmpCommunityExRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,104,2,2,1,5),_H3cSnmpCommunityExRowStatus_Type())
h3cSnmpCommunityExRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSnmpCommunityExRowStatus.setStatus(_A)
_H3cSnmpExtNotifications_ObjectIdentity=ObjectIdentity
h3cSnmpExtNotifications=_H3cSnmpExtNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,104,3))
mibBuilder.exportSymbols(_F,**{'h3cSnmpExt':h3cSnmpExt,'h3cSnmpExtScalarObjects':h3cSnmpExtScalarObjects,'h3cSnmpExtSnmpChannel':h3cSnmpExtSnmpChannel,'h3cSnmpExtReadCommunitySingle':h3cSnmpExtReadCommunitySingle,'h3cSnmpExtWriteCommunitySingle':h3cSnmpExtWriteCommunitySingle,'h3cSnmpExtTables':h3cSnmpExtTables,'h3cSnmpExtCommunityTable':h3cSnmpExtCommunityTable,'h3cSnmpExtCommunityEntry':h3cSnmpExtCommunityEntry,_I:h3cSnmpExtCommunitySecurityLevel,_J:h3cSnmpExtCommunitySecurityName,'h3cSnmpExtCommunityName':h3cSnmpExtCommunityName,'h3cSnmpExtCommunityAclNum':h3cSnmpExtCommunityAclNum,'h3cSnmpCommunityExTable':h3cSnmpCommunityExTable,'h3cSnmpCommunityExEntry':h3cSnmpCommunityExEntry,_L:h3cSnmpCommunityExName,'h3cSnmpCommunityExWrite':h3cSnmpCommunityExWrite,'h3cSnmpCommunityExViewName':h3cSnmpCommunityExViewName,'h3cSnmpCommunityExAclNum':h3cSnmpCommunityExAclNum,'h3cSnmpCommunityExRowStatus':h3cSnmpCommunityExRowStatus,'h3cSnmpExtNotifications':h3cSnmpExtNotifications})