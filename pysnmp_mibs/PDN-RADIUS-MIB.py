_G='sysDevRadiusAuthServerIndex'
_F='PDN-RADIUS-MIB'
_E='DisplayString'
_D='NotificationType'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_radius,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-radius')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_SysDevRadiusMIBObjects_ObjectIdentity=ObjectIdentity
sysDevRadiusMIBObjects=_SysDevRadiusMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,25,1))
class _SysDevRadiusAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SysDevRadiusAuthEnable_Type.__name__=_C
_SysDevRadiusAuthEnable_Object=MibScalar
sysDevRadiusAuthEnable=_SysDevRadiusAuthEnable_Object((1,3,6,1,4,1,1795,2,24,2,25,1,1),_SysDevRadiusAuthEnable_Type())
sysDevRadiusAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthEnable.setStatus(_A)
class _SysDevRadiusAuthTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,30))
_SysDevRadiusAuthTimeout_Type.__name__=_C
_SysDevRadiusAuthTimeout_Object=MibScalar
sysDevRadiusAuthTimeout=_SysDevRadiusAuthTimeout_Object((1,3,6,1,4,1,1795,2,24,2,25,1,2),_SysDevRadiusAuthTimeout_Type())
sysDevRadiusAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthTimeout.setStatus(_A)
class _SysDevRadiusAuthAttempts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SysDevRadiusAuthAttempts_Type.__name__=_C
_SysDevRadiusAuthAttempts_Object=MibScalar
sysDevRadiusAuthAttempts=_SysDevRadiusAuthAttempts_Object((1,3,6,1,4,1,1795,2,24,2,25,1,3),_SysDevRadiusAuthAttempts_Type())
sysDevRadiusAuthAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthAttempts.setStatus(_A)
_SysDevRadiusAuthConfigTable_Object=MibTable
sysDevRadiusAuthConfigTable=_SysDevRadiusAuthConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4))
if mibBuilder.loadTexts:sysDevRadiusAuthConfigTable.setStatus(_A)
_SysDevRadiusAuthConfigEntry_Object=MibTableRow
sysDevRadiusAuthConfigEntry=_SysDevRadiusAuthConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4,1))
sysDevRadiusAuthConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sysDevRadiusAuthConfigEntry.setStatus(_A)
_SysDevRadiusAuthServerIndex_Type=Integer32
_SysDevRadiusAuthServerIndex_Object=MibTableColumn
sysDevRadiusAuthServerIndex=_SysDevRadiusAuthServerIndex_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4,1,1),_SysDevRadiusAuthServerIndex_Type())
sysDevRadiusAuthServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthServerIndex.setStatus(_A)
_SysDevRadiusAuthServerAddress_Type=IpAddress
_SysDevRadiusAuthServerAddress_Object=MibTableColumn
sysDevRadiusAuthServerAddress=_SysDevRadiusAuthServerAddress_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4,1,2),_SysDevRadiusAuthServerAddress_Type())
sysDevRadiusAuthServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthServerAddress.setStatus(_A)
class _SysDevRadiusAuthServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SysDevRadiusAuthServerPort_Type.__name__=_C
_SysDevRadiusAuthServerPort_Object=MibTableColumn
sysDevRadiusAuthServerPort=_SysDevRadiusAuthServerPort_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4,1,3),_SysDevRadiusAuthServerPort_Type())
sysDevRadiusAuthServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDevRadiusAuthServerPort.setStatus(_A)
class _SysDevRadiusAuthSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,32))
_SysDevRadiusAuthSecret_Type.__name__=_E
_SysDevRadiusAuthSecret_Object=MibTableColumn
sysDevRadiusAuthSecret=_SysDevRadiusAuthSecret_Object((1,3,6,1,4,1,1795,2,24,2,25,1,4,1,4),_SysDevRadiusAuthSecret_Type())
sysDevRadiusAuthSecret.setMaxAccess('read-only')
if mibBuilder.loadTexts:sysDevRadiusAuthSecret.setStatus(_A)
_SysDevRadiusMIBTraps_ObjectIdentity=ObjectIdentity
sysDevRadiusMIBTraps=_SysDevRadiusMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,25,2))
mibBuilder.exportSymbols(_F,**{'sysDevRadiusMIBObjects':sysDevRadiusMIBObjects,'sysDevRadiusAuthEnable':sysDevRadiusAuthEnable,'sysDevRadiusAuthTimeout':sysDevRadiusAuthTimeout,'sysDevRadiusAuthAttempts':sysDevRadiusAuthAttempts,'sysDevRadiusAuthConfigTable':sysDevRadiusAuthConfigTable,'sysDevRadiusAuthConfigEntry':sysDevRadiusAuthConfigEntry,_G:sysDevRadiusAuthServerIndex,'sysDevRadiusAuthServerAddress':sysDevRadiusAuthServerAddress,'sysDevRadiusAuthServerPort':sysDevRadiusAuthServerPort,'sysDevRadiusAuthSecret':sysDevRadiusAuthSecret,'sysDevRadiusMIBTraps':sysDevRadiusMIBTraps})