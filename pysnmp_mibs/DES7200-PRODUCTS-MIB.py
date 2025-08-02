if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myModules,mySwitchProducts=mibBuilder.importSymbols('DES7200-SMI','myModules','mySwitchProducts')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
myProductsMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,4,1))
if mibBuilder.loadTexts:myProductsMIB.setRevisions(('2002-03-20 00:00',))
_Des_7206_ObjectIdentity=ObjectIdentity
des_7206=_Des_7206_ObjectIdentity((1,3,6,1,4,1,171,10,97,1,1))
_Des_7210_ObjectIdentity=ObjectIdentity
des_7210=_Des_7210_ObjectIdentity((1,3,6,1,4,1,171,10,97,1,2))
_Des_7206E_ObjectIdentity=ObjectIdentity
des_7206E=_Des_7206E_ObjectIdentity((1,3,6,1,4,1,171,10,97,1,3))
_Des_7210E_ObjectIdentity=ObjectIdentity
des_7210E=_Des_7210E_ObjectIdentity((1,3,6,1,4,1,171,10,97,1,4))
mibBuilder.exportSymbols('DES7200-PRODUCTS-MIB',**{'des-7206':des_7206,'des-7210':des_7210,'des-7206E':des_7206E,'des-7210E':des_7210E,'myProductsMIB':myProductsMIB})