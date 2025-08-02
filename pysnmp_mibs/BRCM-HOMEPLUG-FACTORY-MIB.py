_C='current'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataFactory,=mibBuilder.importSymbols('BRCM-CABLEDATA-FACTORY-MIB','cableDataFactory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_A,'MacAddress','PhysAddress','TextualConvention','TruthValue')
homeplugFactory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,9))
if mibBuilder.loadTexts:homeplugFactory.setRevisions(('2004-12-21 00:00',))
_HomeplugFactMacAddress_Type=MacAddress
_HomeplugFactMacAddress_Object=MibScalar
homeplugFactMacAddress=_HomeplugFactMacAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,2,9,1),_HomeplugFactMacAddress_Type())
homeplugFactMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:homeplugFactMacAddress.setStatus(_C)
class _HomeplugFactDEKPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,24))
_HomeplugFactDEKPassword_Type.__name__=_A
_HomeplugFactDEKPassword_Object=MibScalar
homeplugFactDEKPassword=_HomeplugFactDEKPassword_Object((1,3,6,1,4,1,4413,2,99,1,1,2,9,2),_HomeplugFactDEKPassword_Type())
homeplugFactDEKPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:homeplugFactDEKPassword.setStatus(_C)
class _HomeplugFactNEKPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,24))
_HomeplugFactNEKPassword_Type.__name__=_A
_HomeplugFactNEKPassword_Object=MibScalar
homeplugFactNEKPassword=_HomeplugFactNEKPassword_Object((1,3,6,1,4,1,4413,2,99,1,1,2,9,3),_HomeplugFactNEKPassword_Type())
homeplugFactNEKPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:homeplugFactNEKPassword.setStatus(_C)
mibBuilder.exportSymbols('BRCM-HOMEPLUG-FACTORY-MIB',**{'homeplugFactory':homeplugFactory,'homeplugFactMacAddress':homeplugFactMacAddress,'homeplugFactDEKPassword':homeplugFactDEKPassword,'homeplugFactNEKPassword':homeplugFactNEKPassword})