_G='active'
_F='suspended'
_E='cra'
_D='online'
_C='offline'
_B='other'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoGslbTcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,583))
if mibBuilder.loadTexts:ciscoGslbTcMIB.setRevisions(('2007-02-23 00:00','2006-09-26 00:00'))
class CiscoGslbNodeServices(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('standby',2),('secondary',3)))
class CiscoGslbPeerStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),(_C,2),(_D,3)))
class CiscoGslbAnswerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('vip',2),('ns',3),(_E,4)))
class CiscoGslbKeepaliveTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_B,1),('vip',2),('ns',3),(_E,4),('shared',5)))
class CiscoGslbKeepaliveMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_B,1),('none',2),('icmp',3),('tcp',4),('httphead',5),('kalap',6),('ns',7),(_E,8),('scriptedKal',9)))
class CiscoGslbKeepaliveConfigState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('suspend',2)))
class CiscoGslbKeepaliveRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B,1),('standard',2),('fast',3)))
class CiscoGslbTerminationMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B,1),('reset',2),('graceful',3)))
class CiscoGslbKeepaliveStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_B,1),(_C,2),(_D,3),(_F,4),('init',5)))
class CiscoGslbAnswerStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_B,1),(_C,2),(_D,3),(_F,4),('init',5)))
class CiscoGslbAnswerAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
class CiscoGslbKalapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B,1),('kalapByVip',2),('kalapByTag',3)))
class CiscoGslbBalanceMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_B,1),('orderedList',2),('roundRobin',3),('weightedRR',4),('leastLoaded',5),('hashed',6),('boomerang',7)))
mibBuilder.exportSymbols('CISCO-GSLB-TC-MIB',**{'CiscoGslbNodeServices':CiscoGslbNodeServices,'CiscoGslbPeerStatus':CiscoGslbPeerStatus,'CiscoGslbAnswerType':CiscoGslbAnswerType,'CiscoGslbKeepaliveTargetType':CiscoGslbKeepaliveTargetType,'CiscoGslbKeepaliveMethod':CiscoGslbKeepaliveMethod,'CiscoGslbKeepaliveConfigState':CiscoGslbKeepaliveConfigState,'CiscoGslbKeepaliveRate':CiscoGslbKeepaliveRate,'CiscoGslbTerminationMethod':CiscoGslbTerminationMethod,'CiscoGslbKeepaliveStatus':CiscoGslbKeepaliveStatus,'CiscoGslbAnswerStatus':CiscoGslbAnswerStatus,'CiscoGslbAnswerAdminState':CiscoGslbAnswerAdminState,'CiscoGslbKalapType':CiscoGslbKalapType,'CiscoGslbBalanceMethod':CiscoGslbBalanceMethod,'ciscoGslbTcMIB':ciscoGslbTcMIB})