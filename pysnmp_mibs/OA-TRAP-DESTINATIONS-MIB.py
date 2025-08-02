_T='oaTrapDestGroup'
_S='oaTrapDestInsertHostNameInfo'
_R='oaTrapDestInsertLogInfo'
_Q='oaTrapDestMaxLimit'
_P='oaTrapDestEnableMode'
_O='oaTrapDestAdminStatus'
_N='oaTrapDestTrapType'
_M='oaTrapDestAuthentication'
_L='oaTrapDestVersion'
_K='oaTrapDestGenSupport'
_J='oaTrapDestHostAddress'
_I='read-only'
_H='Unsigned32'
_G='disabled'
_F='enabled'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='OA-TRAP-DESTINATIONS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
oaTrapDestinations=ModuleIdentity((1,3,6,1,4,1,629,1,50,11,1,21))
if mibBuilder.loadTexts:oaTrapDestinations.setRevisions(('2018-06-10 00:00','2012-04-22 00:00','2011-04-12 00:00','2006-12-13 00:00'))
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
class _OaTrapDestGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaTrapDestGenSupport_Type.__name__=_C
_OaTrapDestGenSupport_Object=MibScalar
oaTrapDestGenSupport=_OaTrapDestGenSupport_Object((1,3,6,1,4,1,629,1,50,11,1,21,1),_OaTrapDestGenSupport_Type())
oaTrapDestGenSupport.setMaxAccess(_I)
if mibBuilder.loadTexts:oaTrapDestGenSupport.setStatus(_A)
_OaTrapDestTable_Object=MibTable
oaTrapDestTable=_OaTrapDestTable_Object((1,3,6,1,4,1,629,1,50,11,1,21,2))
if mibBuilder.loadTexts:oaTrapDestTable.setStatus(_A)
_OaTrapDestEntry_Object=MibTableRow
oaTrapDestEntry=_OaTrapDestEntry_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1))
oaTrapDestEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:oaTrapDestEntry.setStatus(_A)
class _OaTrapDestHostAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaTrapDestHostAddress_Type.__name__=_E
_OaTrapDestHostAddress_Object=MibTableColumn
oaTrapDestHostAddress=_OaTrapDestHostAddress_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1,1),_OaTrapDestHostAddress_Type())
oaTrapDestHostAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oaTrapDestHostAddress.setStatus(_A)
class _OaTrapDestVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('other',0),('snmpV1',1),('snmpV2C',2),('snmpV3',3)))
_OaTrapDestVersion_Type.__name__=_C
_OaTrapDestVersion_Object=MibTableColumn
oaTrapDestVersion=_OaTrapDestVersion_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1,2),_OaTrapDestVersion_Type())
oaTrapDestVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestVersion.setStatus(_A)
class _OaTrapDestAuthentication_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaTrapDestAuthentication_Type.__name__=_E
_OaTrapDestAuthentication_Object=MibTableColumn
oaTrapDestAuthentication=_OaTrapDestAuthentication_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1,3),_OaTrapDestAuthentication_Type())
oaTrapDestAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestAuthentication.setStatus(_A)
class _OaTrapDestTrapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('snmpTrap',1),('snmpInform',2)))
_OaTrapDestTrapType_Type.__name__=_C
_OaTrapDestTrapType_Object=MibTableColumn
oaTrapDestTrapType=_OaTrapDestTrapType_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1,4),_OaTrapDestTrapType_Type())
oaTrapDestTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestTrapType.setStatus(_A)
class _OaTrapDestAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_OaTrapDestAdminStatus_Type.__name__=_C
_OaTrapDestAdminStatus_Object=MibTableColumn
oaTrapDestAdminStatus=_OaTrapDestAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,21,2,1,5),_OaTrapDestAdminStatus_Type())
oaTrapDestAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestAdminStatus.setStatus(_A)
class _OaTrapDestEnableMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OaTrapDestEnableMode_Type.__name__=_C
_OaTrapDestEnableMode_Object=MibScalar
oaTrapDestEnableMode=_OaTrapDestEnableMode_Object((1,3,6,1,4,1,629,1,50,11,1,21,3),_OaTrapDestEnableMode_Type())
oaTrapDestEnableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestEnableMode.setStatus(_A)
class _OaTrapDestMaxLimit_Type(Unsigned32):defaultValue=11
_OaTrapDestMaxLimit_Type.__name__=_H
_OaTrapDestMaxLimit_Object=MibScalar
oaTrapDestMaxLimit=_OaTrapDestMaxLimit_Object((1,3,6,1,4,1,629,1,50,11,1,21,4),_OaTrapDestMaxLimit_Type())
oaTrapDestMaxLimit.setMaxAccess(_I)
if mibBuilder.loadTexts:oaTrapDestMaxLimit.setStatus(_A)
class _OaTrapDestInsertLogInfo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OaTrapDestInsertLogInfo_Type.__name__=_C
_OaTrapDestInsertLogInfo_Object=MibScalar
oaTrapDestInsertLogInfo=_OaTrapDestInsertLogInfo_Object((1,3,6,1,4,1,629,1,50,11,1,21,5),_OaTrapDestInsertLogInfo_Type())
oaTrapDestInsertLogInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestInsertLogInfo.setStatus(_A)
class _OaTrapDestInsertHostNameInfo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OaTrapDestInsertHostNameInfo_Type.__name__=_C
_OaTrapDestInsertHostNameInfo_Object=MibScalar
oaTrapDestInsertHostNameInfo=_OaTrapDestInsertHostNameInfo_Object((1,3,6,1,4,1,629,1,50,11,1,21,6),_OaTrapDestInsertHostNameInfo_Type())
oaTrapDestInsertHostNameInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:oaTrapDestInsertHostNameInfo.setStatus(_A)
_OaTrapDestConformance_ObjectIdentity=ObjectIdentity
oaTrapDestConformance=_OaTrapDestConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,21,101))
_OaTrapDestMIBCompliances_ObjectIdentity=ObjectIdentity
oaTrapDestMIBCompliances=_OaTrapDestMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,21,101,1))
_OaTrapDestMIBGroups_ObjectIdentity=ObjectIdentity
oaTrapDestMIBGroups=_OaTrapDestMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,21,101,2))
oaTrapDestGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,21,101,2,1))
oaTrapDestGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:oaTrapDestGroup.setStatus(_A)
oaTrapDestMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,11,1,21,101,1,1))
oaTrapDestMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:oaTrapDestMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'oaTrapDestinations':oaTrapDestinations,_K:oaTrapDestGenSupport,'oaTrapDestTable':oaTrapDestTable,'oaTrapDestEntry':oaTrapDestEntry,_J:oaTrapDestHostAddress,_L:oaTrapDestVersion,_M:oaTrapDestAuthentication,_N:oaTrapDestTrapType,_O:oaTrapDestAdminStatus,_P:oaTrapDestEnableMode,_Q:oaTrapDestMaxLimit,_R:oaTrapDestInsertLogInfo,_S:oaTrapDestInsertHostNameInfo,'oaTrapDestConformance':oaTrapDestConformance,'oaTrapDestMIBCompliances':oaTrapDestMIBCompliances,'oaTrapDestMIBCompliance':oaTrapDestMIBCompliance,'oaTrapDestMIBGroups':oaTrapDestMIBGroups,_T:oaTrapDestGroup})