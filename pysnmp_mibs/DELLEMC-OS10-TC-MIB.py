_e='notPresent'
_d='n3248TEon'
_c='z9332Fon'
_b='s5296Fon'
_a='s5248Fon'
_Z='s5232Fon'
_Y='s5224Fon'
_X='s5212Fon'
_W='z9264Fon'
_V='s4112Ton'
_U='s4112Fon'
_T='s4248FBLon'
_S='s4248FBon'
_R='z9100on'
_Q='s5148Fon'
_P='mx9116Non'
_O='mx5108Non'
_N='s4200on'
_M='s4148Uon'
_L='s4148FEon'
_K='s4128Ton'
_J='s4148Ton'
_I='s4128Fon'
_H='s4148Fon'
_G='s6010on'
_F='s3048on'
_E='s4048Ton'
_D='s4048on'
_C='s6000on'
_B='unknown'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
os10,=mibBuilder.importSymbols('DELLEMC-OS10-SMI-MIB','os10')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
os10TextualConventionsMib=ModuleIdentity((1,3,6,1,4,1,674,11000,5000,100,1))
if mibBuilder.loadTexts:os10TextualConventionsMib.setRevisions(('2019-07-03 12:00','2019-03-07 12:00','2018-05-15 12:00','2018-01-26 12:00','2017-10-27 12:00','2017-10-11 12:00','2017-09-06 12:00','2017-06-21 12:00','2017-01-25 12:00'))
class Os10ChassisDefType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,9999)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4),(_G,5),(_H,6),(_I,7),(_J,8),(_K,9),(_L,10),(_M,11),(_N,12),(_O,13),(_P,14),(_Q,15),(_R,16),(_S,17),(_T,18),(_U,19),(_V,20),(_W,21),('z9224Fon',22),(_X,23),(_Y,24),(_Z,25),(_a,26),(_b,27),(_c,28),(_d,29),(_B,9999)))
class Os10InterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ethernetManagement',1),('ethernet100M',2),('ethernet1GB',3),('ethernet1GBCopper',4),('ethernet10GB',5),('ethernet10GBCopper',6),('ethernet25GB',7),('ethernet50GB',8),('ethernet40GB',9),('ethernet100GB',10),('fc',11)))
class Os10SystemCardType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,9999)));namedValues=NamedValues(*((_e,0),(_C,1),(_D,2),(_E,3),(_F,4),(_G,5),(_H,6),(_I,7),(_J,8),(_K,9),(_L,10),(_M,11),(_N,12),(_O,13),(_P,14),(_Q,15),(_R,16),(_S,17),(_T,18),(_U,19),(_V,20),(_W,21),('z9232Fon',22),(_X,23),(_Y,24),(_Z,25),(_a,26),(_b,27),(_c,28),(_d,29),(_B,9999)))
class Os10CardOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),('cardMisMatch',2),('cardProblem',3),('diagMode',4),('cardAbsent',5),('offline',6)))
class Os10DeviceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('chassis',1),('stack',2),('rpm',3),('supervisor',4),('linecard',5)))
class Os10CmnOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),(_B,4),('dormant',5),(_e,6),('lowerLayerDown',7),('failed',8)))
mibBuilder.exportSymbols('DELLEMC-OS10-TC-MIB',**{'Os10ChassisDefType':Os10ChassisDefType,'Os10InterfaceType':Os10InterfaceType,'Os10SystemCardType':Os10SystemCardType,'Os10CardOperStatus':Os10CardOperStatus,'Os10DeviceType':Os10DeviceType,'Os10CmnOperStatus':Os10CmnOperStatus,'os10TextualConventionsMib':os10TextualConventionsMib})