_D='Integer32'
_C='current'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
ciscoDSGLockLevel=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,22))
if mibBuilder.loadTexts:ciscoDSGLockLevel.setRevisions(('2010-08-30 11:00','2010-06-28 06:00','2010-05-24 06:30','2009-12-20 12:00'))
class _LockLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_LockLevel_Type.__name__=_D
_LockLevel_Object=MibScalar
lockLevel=_LockLevel_Object((1,3,6,1,4,1,1429,2,2,5,22,1),_LockLevel_Type())
lockLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:lockLevel.setStatus(_C)
class _LockLevelPWD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_LockLevelPWD_Type.__name__=_A
_LockLevelPWD_Object=MibScalar
lockLevelPWD=_LockLevelPWD_Object((1,3,6,1,4,1,1429,2,2,5,22,2),_LockLevelPWD_Type())
lockLevelPWD.setMaxAccess(_B)
if mibBuilder.loadTexts:lockLevelPWD.setStatus(_C)
class _LockLevelPWDCUR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_LockLevelPWDCUR_Type.__name__=_A
_LockLevelPWDCUR_Object=MibScalar
lockLevelPWDCUR=_LockLevelPWDCUR_Object((1,3,6,1,4,1,1429,2,2,5,22,3),_LockLevelPWDCUR_Type())
lockLevelPWDCUR.setMaxAccess(_B)
if mibBuilder.loadTexts:lockLevelPWDCUR.setStatus(_C)
class _LockLevelPWDNEW_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_LockLevelPWDNEW_Type.__name__=_A
_LockLevelPWDNEW_Object=MibScalar
lockLevelPWDNEW=_LockLevelPWDNEW_Object((1,3,6,1,4,1,1429,2,2,5,22,4),_LockLevelPWDNEW_Type())
lockLevelPWDNEW.setMaxAccess(_B)
if mibBuilder.loadTexts:lockLevelPWDNEW.setStatus(_C)
class _LockLevelPWDCONF_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_LockLevelPWDCONF_Type.__name__=_A
_LockLevelPWDCONF_Object=MibScalar
lockLevelPWDCONF=_LockLevelPWDCONF_Object((1,3,6,1,4,1,1429,2,2,5,22,5),_LockLevelPWDCONF_Type())
lockLevelPWDCONF.setMaxAccess(_B)
if mibBuilder.loadTexts:lockLevelPWDCONF.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-LOCKLEVEL-MIB',**{'ciscoDSGLockLevel':ciscoDSGLockLevel,'lockLevel':lockLevel,'lockLevelPWD':lockLevelPWD,'lockLevelPWDCUR':lockLevelPWDCUR,'lockLevelPWDNEW':lockLevelPWDNEW,'lockLevelPWDCONF':lockLevelPWDCONF})