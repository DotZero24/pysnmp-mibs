_L='nsVacmAuthType'
_K='NET-SNMP-VACM-MIB'
_J='StorageType'
_I='Integer32'
_H='vacmGroupName'
_G='vacmAccessSecurityModel'
_F='vacmAccessSecurityLevel'
_E='vacmAccessContextPrefix'
_D='SnmpAdminString'
_C='read-create'
_B='SNMP-VIEW-BASED-ACM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netSnmpGroups,netSnmpObjects=mibBuilder.importSymbols('NET-SNMP-MIB','netSnmpGroups','netSnmpObjects')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
vacmAccessContextPrefix,vacmAccessSecurityLevel,vacmAccessSecurityModel,vacmGroupName=mibBuilder.importSymbols(_B,_E,_F,_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention')
netSnmpVacmMIB=ModuleIdentity((1,3,6,1,4,1,8072,1,9))
if mibBuilder.loadTexts:netSnmpVacmMIB.setRevisions(('2006-08-27 00:00',))
_NsVacmAccessTable_Object=MibTable
nsVacmAccessTable=_NsVacmAccessTable_Object((1,3,6,1,4,1,8072,1,9,1))
if mibBuilder.loadTexts:nsVacmAccessTable.setStatus(_A)
_NsVacmAccessEntry_Object=MibTableRow
nsVacmAccessEntry=_NsVacmAccessEntry_Object((1,3,6,1,4,1,8072,1,9,1,1))
nsVacmAccessEntry.setIndexNames((0,_B,_H),(0,_B,_E),(0,_B,_G),(0,_B,_F),(0,_K,_L))
if mibBuilder.loadTexts:nsVacmAccessEntry.setStatus(_A)
class _NsVacmAuthType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVacmAuthType_Type.__name__=_D
_NsVacmAuthType_Object=MibTableColumn
nsVacmAuthType=_NsVacmAuthType_Object((1,3,6,1,4,1,8072,1,9,1,1,1),_NsVacmAuthType_Type())
nsVacmAuthType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nsVacmAuthType.setStatus(_A)
class _NsVacmContextMatch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('prefix',2)))
_NsVacmContextMatch_Type.__name__=_I
_NsVacmContextMatch_Object=MibTableColumn
nsVacmContextMatch=_NsVacmContextMatch_Object((1,3,6,1,4,1,8072,1,9,1,1,2),_NsVacmContextMatch_Type())
nsVacmContextMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVacmContextMatch.setStatus(_A)
class _NsVacmViewName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVacmViewName_Type.__name__=_D
_NsVacmViewName_Object=MibTableColumn
nsVacmViewName=_NsVacmViewName_Object((1,3,6,1,4,1,8072,1,9,1,1,3),_NsVacmViewName_Type())
nsVacmViewName.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVacmViewName.setStatus(_A)
class _NsVacmStorageType_Type(StorageType):defaultValue=3
_NsVacmStorageType_Type.__name__=_J
_NsVacmStorageType_Object=MibTableColumn
nsVacmStorageType=_NsVacmStorageType_Object((1,3,6,1,4,1,8072,1,9,1,1,4),_NsVacmStorageType_Type())
nsVacmStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVacmStorageType.setStatus(_A)
_NsVacmStatus_Type=RowStatus
_NsVacmStatus_Object=MibTableColumn
nsVacmStatus=_NsVacmStatus_Object((1,3,6,1,4,1,8072,1,9,1,1,5),_NsVacmStatus_Type())
nsVacmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVacmStatus.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'netSnmpVacmMIB':netSnmpVacmMIB,'nsVacmAccessTable':nsVacmAccessTable,'nsVacmAccessEntry':nsVacmAccessEntry,_L:nsVacmAuthType,'nsVacmContextMatch':nsVacmContextMatch,'nsVacmViewName':nsVacmViewName,'nsVacmStorageType':nsVacmStorageType,'nsVacmStatus':nsVacmStatus})