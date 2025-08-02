_N='h3cSnmpExtContextName'
_M='h3cSnmpCommunityExName'
_L='h3cSnmpExtCommunitySecurityName'
_K='h3cSnmpExtCommunitySecurityLevel'
_J='TruthValue'
_I='not-accessible'
_H='OctetString'
_G='read-create'
_F='H3C-SNMP-EXT-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='SnmpAdminString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
SnmpAdminString,SnmpSecurityModel=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_B,'SnmpSecurityModel')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
h3cSnmpExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,104))
if mibBuilder.loadTexts:h3cSnmpExt.setRevisions(('2016-08-08 00:00','2016-04-13 02:00','2015-01-20 09:00','2014-08-12 03:03','2013-05-16 00:00','2013-04-08 00:00','2011-08-11 00:00','2010-03-12 00:00','2009-04-07 17:00'))
_H3cSnmpExtScalarObjects_ObjectIdentity=ObjectIdentity
h3cSnmpExtScalarObjects=_H3cSnmpExtScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,1))
class _H3cSnmpExtSnmpChannel_Type(Integer32):defaultValue=161;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSnmpExtSnmpChannel_Type.__name__=_C
_H3cSnmpExtSnmpChannel_Object=MibScalar
h3cSnmpExtSnmpChannel=_H3cSnmpExtSnmpChannel_Object((1,3,6,1,4,1,2011,10,2,104,1,1),_H3cSnmpExtSnmpChannel_Type())
h3cSnmpExtSnmpChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtSnmpChannel.setStatus(_A)
class _H3cSnmpExtReadCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtReadCommunitySingle_Type.__name__=_B
_H3cSnmpExtReadCommunitySingle_Object=MibScalar
h3cSnmpExtReadCommunitySingle=_H3cSnmpExtReadCommunitySingle_Object((1,3,6,1,4,1,2011,10,2,104,1,2),_H3cSnmpExtReadCommunitySingle_Type())
h3cSnmpExtReadCommunitySingle.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtReadCommunitySingle.setStatus(_A)
class _H3cSnmpExtWriteCommunitySingle_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtWriteCommunitySingle_Type.__name__=_B
_H3cSnmpExtWriteCommunitySingle_Object=MibScalar
h3cSnmpExtWriteCommunitySingle=_H3cSnmpExtWriteCommunitySingle_Object((1,3,6,1,4,1,2011,10,2,104,1,3),_H3cSnmpExtWriteCommunitySingle_Type())
h3cSnmpExtWriteCommunitySingle.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtWriteCommunitySingle.setStatus(_A)
class _H3cSnmpExtMaxContextNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSnmpExtMaxContextNum_Type.__name__=_C
_H3cSnmpExtMaxContextNum_Object=MibScalar
h3cSnmpExtMaxContextNum=_H3cSnmpExtMaxContextNum_Object((1,3,6,1,4,1,2011,10,2,104,1,4),_H3cSnmpExtMaxContextNum_Type())
h3cSnmpExtMaxContextNum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtMaxContextNum.setStatus(_A)
class _H3cSnmpExtVersion_Type(Bits):namedValues=NamedValues(*(('snmpV1',0),('snmpV2c',1),('snmpV3',2)))
_H3cSnmpExtVersion_Type.__name__='Bits'
_H3cSnmpExtVersion_Object=MibScalar
h3cSnmpExtVersion=_H3cSnmpExtVersion_Object((1,3,6,1,4,1,2011,10,2,104,1,5),_H3cSnmpExtVersion_Type())
h3cSnmpExtVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtVersion.setStatus(_A)
class _H3cSnmpExtTrapSource_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSnmpExtTrapSource_Type.__name__=_B
_H3cSnmpExtTrapSource_Object=MibScalar
h3cSnmpExtTrapSource=_H3cSnmpExtTrapSource_Object((1,3,6,1,4,1,2011,10,2,104,1,6),_H3cSnmpExtTrapSource_Type())
h3cSnmpExtTrapSource.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtTrapSource.setStatus(_A)
class _H3cSnmpExtInformSource_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSnmpExtInformSource_Type.__name__=_B
_H3cSnmpExtInformSource_Object=MibScalar
h3cSnmpExtInformSource=_H3cSnmpExtInformSource_Object((1,3,6,1,4,1,2011,10,2,104,1,7),_H3cSnmpExtInformSource_Type())
h3cSnmpExtInformSource.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtInformSource.setStatus(_A)
_H3cSnmpExtTables_ObjectIdentity=ObjectIdentity
h3cSnmpExtTables=_H3cSnmpExtTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,2))
_H3cSnmpExtCommunityTable_Object=MibTable
h3cSnmpExtCommunityTable=_H3cSnmpExtCommunityTable_Object((1,3,6,1,4,1,2011,10,2,104,2,1))
if mibBuilder.loadTexts:h3cSnmpExtCommunityTable.setStatus(_A)
_H3cSnmpExtCommunityEntry_Object=MibTableRow
h3cSnmpExtCommunityEntry=_H3cSnmpExtCommunityEntry_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1))
h3cSnmpExtCommunityEntry.setIndexNames((0,_F,_K),(0,_F,_L))
if mibBuilder.loadTexts:h3cSnmpExtCommunityEntry.setStatus(_A)
_H3cSnmpExtCommunitySecurityLevel_Type=SnmpSecurityModel
_H3cSnmpExtCommunitySecurityLevel_Object=MibTableColumn
h3cSnmpExtCommunitySecurityLevel=_H3cSnmpExtCommunitySecurityLevel_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1,1),_H3cSnmpExtCommunitySecurityLevel_Type())
h3cSnmpExtCommunitySecurityLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSnmpExtCommunitySecurityLevel.setStatus(_A)
class _H3cSnmpExtCommunitySecurityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtCommunitySecurityName_Type.__name__=_B
_H3cSnmpExtCommunitySecurityName_Object=MibTableColumn
h3cSnmpExtCommunitySecurityName=_H3cSnmpExtCommunitySecurityName_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1,2),_H3cSnmpExtCommunitySecurityName_Type())
h3cSnmpExtCommunitySecurityName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSnmpExtCommunitySecurityName.setStatus(_A)
class _H3cSnmpExtCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtCommunityName_Type.__name__=_H
_H3cSnmpExtCommunityName_Object=MibTableColumn
h3cSnmpExtCommunityName=_H3cSnmpExtCommunityName_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1,3),_H3cSnmpExtCommunityName_Type())
h3cSnmpExtCommunityName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpExtCommunityName.setStatus(_A)
class _H3cSnmpExtCommunityAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_H3cSnmpExtCommunityAclNum_Type.__name__=_C
_H3cSnmpExtCommunityAclNum_Object=MibTableColumn
h3cSnmpExtCommunityAclNum=_H3cSnmpExtCommunityAclNum_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1,4),_H3cSnmpExtCommunityAclNum_Type())
h3cSnmpExtCommunityAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtCommunityAclNum.setStatus(_A)
class _H3cSnmpExtCommunityIPv6AclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_H3cSnmpExtCommunityIPv6AclNum_Type.__name__=_C
_H3cSnmpExtCommunityIPv6AclNum_Object=MibTableColumn
h3cSnmpExtCommunityIPv6AclNum=_H3cSnmpExtCommunityIPv6AclNum_Object((1,3,6,1,4,1,2011,10,2,104,2,1,1,5),_H3cSnmpExtCommunityIPv6AclNum_Type())
h3cSnmpExtCommunityIPv6AclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSnmpExtCommunityIPv6AclNum.setStatus(_A)
_H3cSnmpCommunityExTable_Object=MibTable
h3cSnmpCommunityExTable=_H3cSnmpCommunityExTable_Object((1,3,6,1,4,1,2011,10,2,104,2,2))
if mibBuilder.loadTexts:h3cSnmpCommunityExTable.setStatus(_A)
_H3cSnmpCommunityExEntry_Object=MibTableRow
h3cSnmpCommunityExEntry=_H3cSnmpCommunityExEntry_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1))
h3cSnmpCommunityExEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:h3cSnmpCommunityExEntry.setStatus(_A)
class _H3cSnmpCommunityExName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpCommunityExName_Type.__name__=_H
_H3cSnmpCommunityExName_Object=MibTableColumn
h3cSnmpCommunityExName=_H3cSnmpCommunityExName_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1,1),_H3cSnmpCommunityExName_Type())
h3cSnmpCommunityExName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSnmpCommunityExName.setStatus(_A)
class _H3cSnmpCommunityExWrite_Type(TruthValue):defaultValue=2
_H3cSnmpCommunityExWrite_Type.__name__=_J
_H3cSnmpCommunityExWrite_Object=MibTableColumn
h3cSnmpCommunityExWrite=_H3cSnmpCommunityExWrite_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1,2),_H3cSnmpCommunityExWrite_Type())
h3cSnmpCommunityExWrite.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnmpCommunityExWrite.setStatus(_A)
class _H3cSnmpCommunityExViewName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpCommunityExViewName_Type.__name__=_H
_H3cSnmpCommunityExViewName_Object=MibTableColumn
h3cSnmpCommunityExViewName=_H3cSnmpCommunityExViewName_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1,3),_H3cSnmpCommunityExViewName_Type())
h3cSnmpCommunityExViewName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnmpCommunityExViewName.setStatus(_A)
class _H3cSnmpCommunityExAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_H3cSnmpCommunityExAclNum_Type.__name__=_C
_H3cSnmpCommunityExAclNum_Object=MibTableColumn
h3cSnmpCommunityExAclNum=_H3cSnmpCommunityExAclNum_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1,4),_H3cSnmpCommunityExAclNum_Type())
h3cSnmpCommunityExAclNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnmpCommunityExAclNum.setStatus(_A)
_H3cSnmpCommunityExRowStatus_Type=RowStatus
_H3cSnmpCommunityExRowStatus_Object=MibTableColumn
h3cSnmpCommunityExRowStatus=_H3cSnmpCommunityExRowStatus_Object((1,3,6,1,4,1,2011,10,2,104,2,2,1,5),_H3cSnmpCommunityExRowStatus_Type())
h3cSnmpCommunityExRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnmpCommunityExRowStatus.setStatus(_A)
_H3cSnmpExtContextTable_Object=MibTable
h3cSnmpExtContextTable=_H3cSnmpExtContextTable_Object((1,3,6,1,4,1,2011,10,2,104,2,3))
if mibBuilder.loadTexts:h3cSnmpExtContextTable.setStatus(_A)
_H3cSnmpExtContextEntry_Object=MibTableRow
h3cSnmpExtContextEntry=_H3cSnmpExtContextEntry_Object((1,3,6,1,4,1,2011,10,2,104,2,3,1))
h3cSnmpExtContextEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:h3cSnmpExtContextEntry.setStatus(_A)
class _H3cSnmpExtContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSnmpExtContextName_Type.__name__=_B
_H3cSnmpExtContextName_Object=MibTableColumn
h3cSnmpExtContextName=_H3cSnmpExtContextName_Object((1,3,6,1,4,1,2011,10,2,104,2,3,1,1),_H3cSnmpExtContextName_Type())
h3cSnmpExtContextName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSnmpExtContextName.setStatus(_A)
_H3cSnmpExtContextRowStatus_Type=RowStatus
_H3cSnmpExtContextRowStatus_Object=MibTableColumn
h3cSnmpExtContextRowStatus=_H3cSnmpExtContextRowStatus_Object((1,3,6,1,4,1,2011,10,2,104,2,3,1,2),_H3cSnmpExtContextRowStatus_Type())
h3cSnmpExtContextRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSnmpExtContextRowStatus.setStatus(_A)
_H3cSnmpExtNotifications_ObjectIdentity=ObjectIdentity
h3cSnmpExtNotifications=_H3cSnmpExtNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,3))
_H3cSnmpExtPrivProtocols_ObjectIdentity=ObjectIdentity
h3cSnmpExtPrivProtocols=_H3cSnmpExtPrivProtocols_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,4))
_H3cSnmpExtAESCfb192PrivProtocol_ObjectIdentity=ObjectIdentity
h3cSnmpExtAESCfb192PrivProtocol=_H3cSnmpExtAESCfb192PrivProtocol_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,4,1))
if mibBuilder.loadTexts:h3cSnmpExtAESCfb192PrivProtocol.setStatus(_A)
_H3cSnmpExtAESCfb256PrivProtocol_ObjectIdentity=ObjectIdentity
h3cSnmpExtAESCfb256PrivProtocol=_H3cSnmpExtAESCfb256PrivProtocol_ObjectIdentity((1,3,6,1,4,1,2011,10,2,104,4,2))
if mibBuilder.loadTexts:h3cSnmpExtAESCfb256PrivProtocol.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'h3cSnmpExt':h3cSnmpExt,'h3cSnmpExtScalarObjects':h3cSnmpExtScalarObjects,'h3cSnmpExtSnmpChannel':h3cSnmpExtSnmpChannel,'h3cSnmpExtReadCommunitySingle':h3cSnmpExtReadCommunitySingle,'h3cSnmpExtWriteCommunitySingle':h3cSnmpExtWriteCommunitySingle,'h3cSnmpExtMaxContextNum':h3cSnmpExtMaxContextNum,'h3cSnmpExtVersion':h3cSnmpExtVersion,'h3cSnmpExtTrapSource':h3cSnmpExtTrapSource,'h3cSnmpExtInformSource':h3cSnmpExtInformSource,'h3cSnmpExtTables':h3cSnmpExtTables,'h3cSnmpExtCommunityTable':h3cSnmpExtCommunityTable,'h3cSnmpExtCommunityEntry':h3cSnmpExtCommunityEntry,_K:h3cSnmpExtCommunitySecurityLevel,_L:h3cSnmpExtCommunitySecurityName,'h3cSnmpExtCommunityName':h3cSnmpExtCommunityName,'h3cSnmpExtCommunityAclNum':h3cSnmpExtCommunityAclNum,'h3cSnmpExtCommunityIPv6AclNum':h3cSnmpExtCommunityIPv6AclNum,'h3cSnmpCommunityExTable':h3cSnmpCommunityExTable,'h3cSnmpCommunityExEntry':h3cSnmpCommunityExEntry,_M:h3cSnmpCommunityExName,'h3cSnmpCommunityExWrite':h3cSnmpCommunityExWrite,'h3cSnmpCommunityExViewName':h3cSnmpCommunityExViewName,'h3cSnmpCommunityExAclNum':h3cSnmpCommunityExAclNum,'h3cSnmpCommunityExRowStatus':h3cSnmpCommunityExRowStatus,'h3cSnmpExtContextTable':h3cSnmpExtContextTable,'h3cSnmpExtContextEntry':h3cSnmpExtContextEntry,_N:h3cSnmpExtContextName,'h3cSnmpExtContextRowStatus':h3cSnmpExtContextRowStatus,'h3cSnmpExtNotifications':h3cSnmpExtNotifications,'h3cSnmpExtPrivProtocols':h3cSnmpExtPrivProtocols,'h3cSnmpExtAESCfb192PrivProtocol':h3cSnmpExtAESCfb192PrivProtocol,'h3cSnmpExtAESCfb256PrivProtocol':h3cSnmpExtAESCfb256PrivProtocol})