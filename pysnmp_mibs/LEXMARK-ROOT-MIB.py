if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lexmarkMIB=ModuleIdentity((1,3,6,1,4,1,641,4,1))
if mibBuilder.loadTexts:lexmarkMIB.setRevisions(('2010-12-01 23:00','2009-11-24 20:40'))
_Lexmark_ObjectIdentity=ObjectIdentity
lexmark=_Lexmark_ObjectIdentity((1,3,6,1,4,1,641))
_LexmarkModules_ObjectIdentity=ObjectIdentity
lexmarkModules=_LexmarkModules_ObjectIdentity((1,3,6,1,4,1,641,4))
_LexmarkMibObjects_ObjectIdentity=ObjectIdentity
lexmarkMibObjects=_LexmarkMibObjects_ObjectIdentity((1,3,6,1,4,1,641,5))
mibBuilder.exportSymbols('LEXMARK-ROOT-MIB',**{'lexmark':lexmark,'lexmarkModules':lexmarkModules,'lexmarkMIB':lexmarkMIB,'lexmarkMibObjects':lexmarkMibObjects})