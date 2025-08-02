_H='dpStormCtrlBaiscGroup'
_G='dpStormCtrlCurTrafficValue'
_F='dpStormCtrlCurTrafficType'
_E='read-write'
_D='ifIndex'
_C='IF-MIB'
_B='DLINKPRIME-STORM-CTRL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndex',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlinkPrimeStormCtrlMIB=ModuleIdentity((1,3,6,1,4,1,171,15,17))
if mibBuilder.loadTexts:dlinkPrimeStormCtrlMIB.setRevisions(('2014-04-26 00:00',))
class DpStormCtlTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('broadcast',2),('multicast',3),('unicast',4)))
class DpStormCtlThrTypeValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('noLimit',1),('limit_512Kbps',2),('limit_1Mbps',3),('limit_2Mbps',4),('limit_4Mbps',5),('limit_8Mbps',6),('limit_16Mbps',7),('limit_32Mbps',8),('limit_64Mbps',9),('limit_128Mbps',10),('limit_256Mbps',11),('limit_512Mbps',12)))
_DpStormCtrlMIBObjects_ObjectIdentity=ObjectIdentity
dpStormCtrlMIBObjects=_DpStormCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,17,1))
_DpStormCtrlTrafficInfoTable_Object=MibTable
dpStormCtrlTrafficInfoTable=_DpStormCtrlTrafficInfoTable_Object((1,3,6,1,4,1,171,15,17,1,1))
if mibBuilder.loadTexts:dpStormCtrlTrafficInfoTable.setStatus(_A)
_DpStormCtrlTrafficInfoEntry_Object=MibTableRow
dpStormCtrlTrafficInfoEntry=_DpStormCtrlTrafficInfoEntry_Object((1,3,6,1,4,1,171,15,17,1,1,1))
dpStormCtrlTrafficInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dpStormCtrlTrafficInfoEntry.setStatus(_A)
_DpStormCtrlCurTrafficType_Type=DpStormCtlTrafficType
_DpStormCtrlCurTrafficType_Object=MibTableColumn
dpStormCtrlCurTrafficType=_DpStormCtrlCurTrafficType_Object((1,3,6,1,4,1,171,15,17,1,1,1,1),_DpStormCtrlCurTrafficType_Type())
dpStormCtrlCurTrafficType.setMaxAccess(_E)
if mibBuilder.loadTexts:dpStormCtrlCurTrafficType.setStatus(_A)
_DpStormCtrlCurTrafficValue_Type=DpStormCtlThrTypeValue
_DpStormCtrlCurTrafficValue_Object=MibTableColumn
dpStormCtrlCurTrafficValue=_DpStormCtrlCurTrafficValue_Object((1,3,6,1,4,1,171,15,17,1,1,1,2),_DpStormCtrlCurTrafficValue_Type())
dpStormCtrlCurTrafficValue.setMaxAccess(_E)
if mibBuilder.loadTexts:dpStormCtrlCurTrafficValue.setStatus(_A)
_DpStormCtrlMIBConformance_ObjectIdentity=ObjectIdentity
dpStormCtrlMIBConformance=_DpStormCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,17,2))
_DpStormCtrlCompliances_ObjectIdentity=ObjectIdentity
dpStormCtrlCompliances=_DpStormCtrlCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,17,2,1))
_DpStormCtrlGroup_ObjectIdentity=ObjectIdentity
dpStormCtrlGroup=_DpStormCtrlGroup_ObjectIdentity((1,3,6,1,4,1,171,15,17,2,2))
dpStormCtrlBaiscGroup=ObjectGroup((1,3,6,1,4,1,171,15,17,2,2,1))
dpStormCtrlBaiscGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:dpStormCtrlBaiscGroup.setStatus(_A)
dpStormCtrlCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,17,2,1,1))
dpStormCtrlCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:dpStormCtrlCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DpStormCtlTrafficType':DpStormCtlTrafficType,'DpStormCtlThrTypeValue':DpStormCtlThrTypeValue,'dlinkPrimeStormCtrlMIB':dlinkPrimeStormCtrlMIB,'dpStormCtrlMIBObjects':dpStormCtrlMIBObjects,'dpStormCtrlTrafficInfoTable':dpStormCtrlTrafficInfoTable,'dpStormCtrlTrafficInfoEntry':dpStormCtrlTrafficInfoEntry,_F:dpStormCtrlCurTrafficType,_G:dpStormCtrlCurTrafficValue,'dpStormCtrlMIBConformance':dpStormCtrlMIBConformance,'dpStormCtrlCompliances':dpStormCtrlCompliances,'dpStormCtrlCompliance':dpStormCtrlCompliance,'dpStormCtrlGroup':dpStormCtrlGroup,_H:dpStormCtrlBaiscGroup})