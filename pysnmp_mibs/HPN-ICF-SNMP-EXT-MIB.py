_N='hpnicfSnmpExtContextName'
_M='hpnicfSnmpCommunityExName'
_L='hpnicfSnmpExtCommunitySecurityName'
_K='hpnicfSnmpExtCommunitySecurityLevel'
_J='TruthValue'
_I='not-accessible'
_H='read-only'
_G='read-write'
_F='OctetString'
_E='read-create'
_D='HPN-ICF-SNMP-EXT-MIB'
_C='Integer32'
_B='SnmpAdminString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
SnmpAdminString,SnmpSecurityModel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_B,'SnmpSecurityModel')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
hpnicfSnmpExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,104))
if mibBuilder.loadTexts:hpnicfSnmpExt.setRevisions(('2009-04-07 17:00',))
_HpnicfSnmpExtScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfSnmpExtScalarObjects=_HpnicfSnmpExtScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,104,1))
class _HpnicfSnmpExtSnmpChannel_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSnmpExtSnmpChannel_Type.__name__=_C
_HpnicfSnmpExtSnmpChannel_Object=MibScalar
hpnicfSnmpExtSnmpChannel=_HpnicfSnmpExtSnmpChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,1,1),_HpnicfSnmpExtSnmpChannel_Type())
hpnicfSnmpExtSnmpChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSnmpExtSnmpChannel.setStatus(_A)
class _HpnicfSnmpExtReadCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpExtReadCommunitySingle_Type.__name__=_B
_HpnicfSnmpExtReadCommunitySingle_Object=MibScalar
hpnicfSnmpExtReadCommunitySingle=_HpnicfSnmpExtReadCommunitySingle_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,1,2),_HpnicfSnmpExtReadCommunitySingle_Type())
hpnicfSnmpExtReadCommunitySingle.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSnmpExtReadCommunitySingle.setStatus(_A)
class _HpnicfSnmpExtWriteCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpExtWriteCommunitySingle_Type.__name__=_B
_HpnicfSnmpExtWriteCommunitySingle_Object=MibScalar
hpnicfSnmpExtWriteCommunitySingle=_HpnicfSnmpExtWriteCommunitySingle_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,1,3),_HpnicfSnmpExtWriteCommunitySingle_Type())
hpnicfSnmpExtWriteCommunitySingle.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSnmpExtWriteCommunitySingle.setStatus(_A)
class _HpnicfSnmpExtMaxContextNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSnmpExtMaxContextNum_Type.__name__=_C
_HpnicfSnmpExtMaxContextNum_Object=MibScalar
hpnicfSnmpExtMaxContextNum=_HpnicfSnmpExtMaxContextNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,1,4),_HpnicfSnmpExtMaxContextNum_Type())
hpnicfSnmpExtMaxContextNum.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSnmpExtMaxContextNum.setStatus(_A)
_HpnicfSnmpExtTables_ObjectIdentity=ObjectIdentity
hpnicfSnmpExtTables=_HpnicfSnmpExtTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,104,2))
_HpnicfSnmpExtCommunityTable_Object=MibTable
hpnicfSnmpExtCommunityTable=_HpnicfSnmpExtCommunityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1))
if mibBuilder.loadTexts:hpnicfSnmpExtCommunityTable.setStatus(_A)
_HpnicfSnmpExtCommunityEntry_Object=MibTableRow
hpnicfSnmpExtCommunityEntry=_HpnicfSnmpExtCommunityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1,1))
hpnicfSnmpExtCommunityEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:hpnicfSnmpExtCommunityEntry.setStatus(_A)
_HpnicfSnmpExtCommunitySecurityLevel_Type=SnmpSecurityModel
_HpnicfSnmpExtCommunitySecurityLevel_Object=MibTableColumn
hpnicfSnmpExtCommunitySecurityLevel=_HpnicfSnmpExtCommunitySecurityLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1,1,1),_HpnicfSnmpExtCommunitySecurityLevel_Type())
hpnicfSnmpExtCommunitySecurityLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfSnmpExtCommunitySecurityLevel.setStatus(_A)
class _HpnicfSnmpExtCommunitySecurityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpExtCommunitySecurityName_Type.__name__=_B
_HpnicfSnmpExtCommunitySecurityName_Object=MibTableColumn
hpnicfSnmpExtCommunitySecurityName=_HpnicfSnmpExtCommunitySecurityName_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1,1,2),_HpnicfSnmpExtCommunitySecurityName_Type())
hpnicfSnmpExtCommunitySecurityName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfSnmpExtCommunitySecurityName.setStatus(_A)
class _HpnicfSnmpExtCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpExtCommunityName_Type.__name__=_F
_HpnicfSnmpExtCommunityName_Object=MibTableColumn
hpnicfSnmpExtCommunityName=_HpnicfSnmpExtCommunityName_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1,1,3),_HpnicfSnmpExtCommunityName_Type())
hpnicfSnmpExtCommunityName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSnmpExtCommunityName.setStatus(_A)
class _HpnicfSnmpExtCommunityAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_HpnicfSnmpExtCommunityAclNum_Type.__name__=_C
_HpnicfSnmpExtCommunityAclNum_Object=MibTableColumn
hpnicfSnmpExtCommunityAclNum=_HpnicfSnmpExtCommunityAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,1,1,4),_HpnicfSnmpExtCommunityAclNum_Type())
hpnicfSnmpExtCommunityAclNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSnmpExtCommunityAclNum.setStatus(_A)
_HpnicfSnmpCommunityExTable_Object=MibTable
hpnicfSnmpCommunityExTable=_HpnicfSnmpCommunityExTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2))
if mibBuilder.loadTexts:hpnicfSnmpCommunityExTable.setStatus(_A)
_HpnicfSnmpCommunityExEntry_Object=MibTableRow
hpnicfSnmpCommunityExEntry=_HpnicfSnmpCommunityExEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1))
hpnicfSnmpCommunityExEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:hpnicfSnmpCommunityExEntry.setStatus(_A)
class _HpnicfSnmpCommunityExName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpCommunityExName_Type.__name__=_F
_HpnicfSnmpCommunityExName_Object=MibTableColumn
hpnicfSnmpCommunityExName=_HpnicfSnmpCommunityExName_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1,1),_HpnicfSnmpCommunityExName_Type())
hpnicfSnmpCommunityExName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSnmpCommunityExName.setStatus(_A)
class _HpnicfSnmpCommunityExWrite_Type(TruthValue):defaultValue=2
_HpnicfSnmpCommunityExWrite_Type.__name__=_J
_HpnicfSnmpCommunityExWrite_Object=MibTableColumn
hpnicfSnmpCommunityExWrite=_HpnicfSnmpCommunityExWrite_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1,2),_HpnicfSnmpCommunityExWrite_Type())
hpnicfSnmpCommunityExWrite.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSnmpCommunityExWrite.setStatus(_A)
class _HpnicfSnmpCommunityExViewName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpCommunityExViewName_Type.__name__=_F
_HpnicfSnmpCommunityExViewName_Object=MibTableColumn
hpnicfSnmpCommunityExViewName=_HpnicfSnmpCommunityExViewName_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1,3),_HpnicfSnmpCommunityExViewName_Type())
hpnicfSnmpCommunityExViewName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSnmpCommunityExViewName.setStatus(_A)
class _HpnicfSnmpCommunityExAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_HpnicfSnmpCommunityExAclNum_Type.__name__=_C
_HpnicfSnmpCommunityExAclNum_Object=MibTableColumn
hpnicfSnmpCommunityExAclNum=_HpnicfSnmpCommunityExAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1,4),_HpnicfSnmpCommunityExAclNum_Type())
hpnicfSnmpCommunityExAclNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSnmpCommunityExAclNum.setStatus(_A)
_HpnicfSnmpCommunityExRowStatus_Type=RowStatus
_HpnicfSnmpCommunityExRowStatus_Object=MibTableColumn
hpnicfSnmpCommunityExRowStatus=_HpnicfSnmpCommunityExRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,2,1,5),_HpnicfSnmpCommunityExRowStatus_Type())
hpnicfSnmpCommunityExRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSnmpCommunityExRowStatus.setStatus(_A)
_HpnicfSnmpExtContextTable_Object=MibTable
hpnicfSnmpExtContextTable=_HpnicfSnmpExtContextTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,3))
if mibBuilder.loadTexts:hpnicfSnmpExtContextTable.setStatus(_A)
_HpnicfSnmpExtContextEntry_Object=MibTableRow
hpnicfSnmpExtContextEntry=_HpnicfSnmpExtContextEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,3,1))
hpnicfSnmpExtContextEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:hpnicfSnmpExtContextEntry.setStatus(_A)
class _HpnicfSnmpExtContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfSnmpExtContextName_Type.__name__=_B
_HpnicfSnmpExtContextName_Object=MibTableColumn
hpnicfSnmpExtContextName=_HpnicfSnmpExtContextName_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,3,1,1),_HpnicfSnmpExtContextName_Type())
hpnicfSnmpExtContextName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfSnmpExtContextName.setStatus(_A)
_HpnicfSnmpExtContextRowStatus_Type=RowStatus
_HpnicfSnmpExtContextRowStatus_Object=MibTableColumn
hpnicfSnmpExtContextRowStatus=_HpnicfSnmpExtContextRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,104,2,3,1,2),_HpnicfSnmpExtContextRowStatus_Type())
hpnicfSnmpExtContextRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSnmpExtContextRowStatus.setStatus(_A)
_HpnicfSnmpExtNotifications_ObjectIdentity=ObjectIdentity
hpnicfSnmpExtNotifications=_HpnicfSnmpExtNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,104,3))
mibBuilder.exportSymbols(_D,**{'hpnicfSnmpExt':hpnicfSnmpExt,'hpnicfSnmpExtScalarObjects':hpnicfSnmpExtScalarObjects,'hpnicfSnmpExtSnmpChannel':hpnicfSnmpExtSnmpChannel,'hpnicfSnmpExtReadCommunitySingle':hpnicfSnmpExtReadCommunitySingle,'hpnicfSnmpExtWriteCommunitySingle':hpnicfSnmpExtWriteCommunitySingle,'hpnicfSnmpExtMaxContextNum':hpnicfSnmpExtMaxContextNum,'hpnicfSnmpExtTables':hpnicfSnmpExtTables,'hpnicfSnmpExtCommunityTable':hpnicfSnmpExtCommunityTable,'hpnicfSnmpExtCommunityEntry':hpnicfSnmpExtCommunityEntry,_K:hpnicfSnmpExtCommunitySecurityLevel,_L:hpnicfSnmpExtCommunitySecurityName,'hpnicfSnmpExtCommunityName':hpnicfSnmpExtCommunityName,'hpnicfSnmpExtCommunityAclNum':hpnicfSnmpExtCommunityAclNum,'hpnicfSnmpCommunityExTable':hpnicfSnmpCommunityExTable,'hpnicfSnmpCommunityExEntry':hpnicfSnmpCommunityExEntry,_M:hpnicfSnmpCommunityExName,'hpnicfSnmpCommunityExWrite':hpnicfSnmpCommunityExWrite,'hpnicfSnmpCommunityExViewName':hpnicfSnmpCommunityExViewName,'hpnicfSnmpCommunityExAclNum':hpnicfSnmpCommunityExAclNum,'hpnicfSnmpCommunityExRowStatus':hpnicfSnmpCommunityExRowStatus,'hpnicfSnmpExtContextTable':hpnicfSnmpExtContextTable,'hpnicfSnmpExtContextEntry':hpnicfSnmpExtContextEntry,_N:hpnicfSnmpExtContextName,'hpnicfSnmpExtContextRowStatus':hpnicfSnmpExtContextRowStatus,'hpnicfSnmpExtNotifications':hpnicfSnmpExtNotifications})