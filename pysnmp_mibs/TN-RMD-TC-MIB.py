_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnRmdMIBModules,=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnRmdMIBModules')
tnRmdTcModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,4,5))
if mibBuilder.loadTexts:tnRmdTcModule.setRevisions(('2018-02-23 12:00','2016-11-16 00:00','2013-08-09 00:00','2012-11-28 00:00'))
class TnRmdAccessIfIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
class TnRmdInventory(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
class TnRmdPcp(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class TnRmdTpid(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class TnRmdVersion(DisplayString):status=_A
class TnRmdItemCode(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
class TnRmdOui(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class TnRmdUserLabel(DisplayString):status=_A
mibBuilder.exportSymbols('TN-RMD-TC-MIB',**{'TnRmdAccessIfIndex':TnRmdAccessIfIndex,'TnRmdInventory':TnRmdInventory,'TnRmdPcp':TnRmdPcp,'TnRmdTpid':TnRmdTpid,'TnRmdVersion':TnRmdVersion,'TnRmdItemCode':TnRmdItemCode,'TnRmdOui':TnRmdOui,'TnRmdUserLabel':TnRmdUserLabel,'tnRmdTcModule':tnRmdTcModule})