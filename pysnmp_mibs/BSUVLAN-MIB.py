_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniBsuVlan=ModuleIdentity((1,3,6,1,4,1,4325,3,11))
_AniBsuVlanConf_ObjectIdentity=ObjectIdentity
aniBsuVlanConf=_AniBsuVlanConf_ObjectIdentity((1,3,6,1,4,1,4325,3,11,1))
class _AniBsuVlanConfMgmtVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AniBsuVlanConfMgmtVlanId_Type.__name__=_A
_AniBsuVlanConfMgmtVlanId_Object=MibScalar
aniBsuVlanConfMgmtVlanId=_AniBsuVlanConfMgmtVlanId_Object((1,3,6,1,4,1,4325,3,11,1,1),_AniBsuVlanConfMgmtVlanId_Type())
aniBsuVlanConfMgmtVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuVlanConfMgmtVlanId.setStatus(_C)
class _AniBsuVlanConfOuterTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AniBsuVlanConfOuterTagId_Type.__name__=_A
_AniBsuVlanConfOuterTagId_Object=MibScalar
aniBsuVlanConfOuterTagId=_AniBsuVlanConfOuterTagId_Object((1,3,6,1,4,1,4325,3,11,1,4),_AniBsuVlanConfOuterTagId_Type())
aniBsuVlanConfOuterTagId.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuVlanConfOuterTagId.setStatus(_C)
class _AniBsuVlanConfMgmtVlanIdPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AniBsuVlanConfMgmtVlanIdPriority_Type.__name__=_A
_AniBsuVlanConfMgmtVlanIdPriority_Object=MibScalar
aniBsuVlanConfMgmtVlanIdPriority=_AniBsuVlanConfMgmtVlanIdPriority_Object((1,3,6,1,4,1,4325,3,11,1,5),_AniBsuVlanConfMgmtVlanIdPriority_Type())
aniBsuVlanConfMgmtVlanIdPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuVlanConfMgmtVlanIdPriority.setStatus(_C)
class _AniBsuVlanConfOuterTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AniBsuVlanConfOuterTagPriority_Type.__name__=_A
_AniBsuVlanConfOuterTagPriority_Object=MibScalar
aniBsuVlanConfOuterTagPriority=_AniBsuVlanConfOuterTagPriority_Object((1,3,6,1,4,1,4325,3,11,1,6),_AniBsuVlanConfOuterTagPriority_Type())
aniBsuVlanConfOuterTagPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuVlanConfOuterTagPriority.setStatus(_C)
_AniBsuVlanConfSUMgmtVlanIdList_Type=DisplayString
_AniBsuVlanConfSUMgmtVlanIdList_Object=MibScalar
aniBsuVlanConfSUMgmtVlanIdList=_AniBsuVlanConfSUMgmtVlanIdList_Object((1,3,6,1,4,1,4325,3,11,1,7),_AniBsuVlanConfSUMgmtVlanIdList_Type())
aniBsuVlanConfSUMgmtVlanIdList.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuVlanConfSUMgmtVlanIdList.setStatus(_C)
mibBuilder.exportSymbols('BSUVLAN-MIB',**{'aniBsuVlan':aniBsuVlan,'aniBsuVlanConf':aniBsuVlanConf,'aniBsuVlanConfMgmtVlanId':aniBsuVlanConfMgmtVlanId,'aniBsuVlanConfOuterTagId':aniBsuVlanConfOuterTagId,'aniBsuVlanConfMgmtVlanIdPriority':aniBsuVlanConfMgmtVlanIdPriority,'aniBsuVlanConfOuterTagPriority':aniBsuVlanConfOuterTagPriority,'aniBsuVlanConfSUMgmtVlanIdList':aniBsuVlanConfSUMgmtVlanIdList})