_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
aerohive=ModuleIdentity((1,3,6,1,4,1,26928))
class AhString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class AhNodeID(MacAddress):status=_A
class AhInterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ahPHYSICAL',0),('ahVIRTURAL',1)))
class AhInterfaceMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ahNotUsed',0),('ahAccess',1),('ahBackhaul',2),('ahBridge',3)))
class AhMACProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ah11a',0),('ah11b',1),('ah11g',2),('ah11na',3),('ah11ng',4)))
_AhProduct_ObjectIdentity=ObjectIdentity
ahProduct=_AhProduct_ObjectIdentity((1,3,6,1,4,1,26928,1))
_AhAP_ObjectIdentity=ObjectIdentity
ahAP=_AhAP_ObjectIdentity((1,3,6,1,4,1,26928,1,1))
_AhAPCommon_ObjectIdentity=ObjectIdentity
ahAPCommon=_AhAPCommon_ObjectIdentity((1,3,6,1,4,1,26928,1,1,1))
_AhAPTrap_ObjectIdentity=ObjectIdentity
ahAPTrap=_AhAPTrap_ObjectIdentity((1,3,6,1,4,1,26928,1,1,1,1))
_AhAPInterface_ObjectIdentity=ObjectIdentity
ahAPInterface=_AhAPInterface_ObjectIdentity((1,3,6,1,4,1,26928,1,1,1,2))
_AhAPMRP_ObjectIdentity=ObjectIdentity
ahAPMRP=_AhAPMRP_ObjectIdentity((1,3,6,1,4,1,26928,1,1,1,3))
_AhAPIDP_ObjectIdentity=ObjectIdentity
ahAPIDP=_AhAPIDP_ObjectIdentity((1,3,6,1,4,1,26928,1,1,1,4))
_AhAPHiveAP020_ag_ObjectIdentity=ObjectIdentity
ahAPHiveAP020_ag=_AhAPHiveAP020_ag_ObjectIdentity((1,3,6,1,4,1,26928,1,1,2))
_AhAPHiveAP028_ag_ObjectIdentity=ObjectIdentity
ahAPHiveAP028_ag=_AhAPHiveAP028_ag_ObjectIdentity((1,3,6,1,4,1,26928,1,1,3))
_AhAPHiveAP320_n_ObjectIdentity=ObjectIdentity
ahAPHiveAP320_n=_AhAPHiveAP320_n_ObjectIdentity((1,3,6,1,4,1,26928,1,1,4))
_AhAPHiveAP340_n_ObjectIdentity=ObjectIdentity
ahAPHiveAP340_n=_AhAPHiveAP340_n_ObjectIdentity((1,3,6,1,4,1,26928,1,1,5))
mibBuilder.exportSymbols('AH-SMI-MIB',**{'AhString':AhString,'AhNodeID':AhNodeID,'AhInterfaceType':AhInterfaceType,'AhInterfaceMode':AhInterfaceMode,'AhMACProtocol':AhMACProtocol,'aerohive':aerohive,'ahProduct':ahProduct,'ahAP':ahAP,'ahAPCommon':ahAPCommon,'ahAPTrap':ahAPTrap,'ahAPInterface':ahAPInterface,'ahAPMRP':ahAPMRP,'ahAPIDP':ahAPIDP,'ahAPHiveAP020-ag':ahAPHiveAP020_ag,'ahAPHiveAP028-ag':ahAPHiveAP028_ag,'ahAPHiveAP320-n':ahAPHiveAP320_n,'ahAPHiveAP340-n':ahAPHiveAP340_n})