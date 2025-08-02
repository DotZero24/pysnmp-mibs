_B='current'
_A='accessible-for-notify'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCommon,=mibBuilder.importSymbols('CIENA-SMI','cienaCommon')
CienaGlobalSeverity,=mibBuilder.importSymbols('CIENA-TC','CienaGlobalSeverity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
cienaGlobal=ModuleIdentity((1,3,6,1,4,1,1271,1,3))
if mibBuilder.loadTexts:cienaGlobal.setRevisions(('2017-06-07 00:00','2010-03-28 00:00'))
_CienaGlobalSeverity_Type=CienaGlobalSeverity
_CienaGlobalSeverity_Object=MibScalar
cienaGlobalSeverity=_CienaGlobalSeverity_Object((1,3,6,1,4,1,1271,1,3,1),_CienaGlobalSeverity_Type())
cienaGlobalSeverity.setMaxAccess(_A)
if mibBuilder.loadTexts:cienaGlobalSeverity.setStatus(_B)
_CienaGlobalMacAddress_Type=MacAddress
_CienaGlobalMacAddress_Object=MibScalar
cienaGlobalMacAddress=_CienaGlobalMacAddress_Object((1,3,6,1,4,1,1271,1,3,2),_CienaGlobalMacAddress_Type())
cienaGlobalMacAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cienaGlobalMacAddress.setStatus(_B)
mibBuilder.exportSymbols('CIENA-GLOBAL-MIB',**{'cienaGlobal':cienaGlobal,'cienaGlobalSeverity':cienaGlobalSeverity,'cienaGlobalMacAddress':cienaGlobalMacAddress})