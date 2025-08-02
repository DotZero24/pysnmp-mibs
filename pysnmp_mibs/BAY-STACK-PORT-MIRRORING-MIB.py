_H='bsPortMirroringRspanInstance'
_G='not-accessible'
_F='bsPortMirroringCtrlInstance'
_E='BAY-STACK-PORT-MIRRORING-MIB'
_D='PortList'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackPortMirroringMib=ModuleIdentity((1,3,6,1,4,1,45,5,28))
if mibBuilder.loadTexts:bayStackPortMirroringMib.setRevisions(('2015-12-03 00:00','2012-10-10 00:00','2009-05-28 00:00','2008-01-18 00:00'))
_BsPortMirroringNotifications_ObjectIdentity=ObjectIdentity
bsPortMirroringNotifications=_BsPortMirroringNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,28,0))
_BsPortMirroringObjects_ObjectIdentity=ObjectIdentity
bsPortMirroringObjects=_BsPortMirroringObjects_ObjectIdentity((1,3,6,1,4,1,45,5,28,1))
_BsPortMirroringCtrlTable_Object=MibTable
bsPortMirroringCtrlTable=_BsPortMirroringCtrlTable_Object((1,3,6,1,4,1,45,5,28,1,1))
if mibBuilder.loadTexts:bsPortMirroringCtrlTable.setStatus(_A)
_BsPortMirroringCtrlEntry_Object=MibTableRow
bsPortMirroringCtrlEntry=_BsPortMirroringCtrlEntry_Object((1,3,6,1,4,1,45,5,28,1,1,1))
bsPortMirroringCtrlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bsPortMirroringCtrlEntry.setStatus(_A)
class _BsPortMirroringCtrlInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BsPortMirroringCtrlInstance_Type.__name__=_C
_BsPortMirroringCtrlInstance_Object=MibTableColumn
bsPortMirroringCtrlInstance=_BsPortMirroringCtrlInstance_Object((1,3,6,1,4,1,45,5,28,1,1,1,1),_BsPortMirroringCtrlInstance_Type())
bsPortMirroringCtrlInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:bsPortMirroringCtrlInstance.setStatus(_A)
class _BsPortMirroringCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('disable',1),('adst',2),('asrc',3),('asrcBdst',4),('asrcBdstOrBsrcAdst',5),('asrcOrAdst',6),('manytoOneRx',7),('manytoOneRxTx',8),('manytoOneTx',9),('xrx',10),('xrxOrXtx',11),('xrxOrYtx',12),('xrxYtx',13),('xrxYtxOrYrxXtx',14),('xtx',15)))
_BsPortMirroringCtrlPortMode_Type.__name__=_C
_BsPortMirroringCtrlPortMode_Object=MibTableColumn
bsPortMirroringCtrlPortMode=_BsPortMirroringCtrlPortMode_Object((1,3,6,1,4,1,45,5,28,1,1,1,2),_BsPortMirroringCtrlPortMode_Type())
bsPortMirroringCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlPortMode.setStatus(_A)
_BsPortMirroringCtrlMonitorPort_Type=InterfaceIndex
_BsPortMirroringCtrlMonitorPort_Object=MibTableColumn
bsPortMirroringCtrlMonitorPort=_BsPortMirroringCtrlMonitorPort_Object((1,3,6,1,4,1,45,5,28,1,1,1,3),_BsPortMirroringCtrlMonitorPort_Type())
bsPortMirroringCtrlMonitorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlMonitorPort.setStatus(_A)
class _BsPortMirroringCtrlPortListX_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BsPortMirroringCtrlPortListX_Type.__name__=_D
_BsPortMirroringCtrlPortListX_Object=MibTableColumn
bsPortMirroringCtrlPortListX=_BsPortMirroringCtrlPortListX_Object((1,3,6,1,4,1,45,5,28,1,1,1,4),_BsPortMirroringCtrlPortListX_Type())
bsPortMirroringCtrlPortListX.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlPortListX.setStatus(_A)
class _BsPortMirroringCtrlPortListY_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BsPortMirroringCtrlPortListY_Type.__name__=_D
_BsPortMirroringCtrlPortListY_Object=MibTableColumn
bsPortMirroringCtrlPortListY=_BsPortMirroringCtrlPortListY_Object((1,3,6,1,4,1,45,5,28,1,1,1,5),_BsPortMirroringCtrlPortListY_Type())
bsPortMirroringCtrlPortListY.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlPortListY.setStatus(_A)
_BsPortMirroringCtrlMacAddressA_Type=MacAddress
_BsPortMirroringCtrlMacAddressA_Object=MibTableColumn
bsPortMirroringCtrlMacAddressA=_BsPortMirroringCtrlMacAddressA_Object((1,3,6,1,4,1,45,5,28,1,1,1,6),_BsPortMirroringCtrlMacAddressA_Type())
bsPortMirroringCtrlMacAddressA.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlMacAddressA.setStatus(_A)
_BsPortMirroringCtrlMacAddressB_Type=MacAddress
_BsPortMirroringCtrlMacAddressB_Object=MibTableColumn
bsPortMirroringCtrlMacAddressB=_BsPortMirroringCtrlMacAddressB_Object((1,3,6,1,4,1,45,5,28,1,1,1,7),_BsPortMirroringCtrlMacAddressB_Type())
bsPortMirroringCtrlMacAddressB.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlMacAddressB.setStatus(_A)
_BsPortMirroringCtrlRowStatus_Type=RowStatus
_BsPortMirroringCtrlRowStatus_Object=MibTableColumn
bsPortMirroringCtrlRowStatus=_BsPortMirroringCtrlRowStatus_Object((1,3,6,1,4,1,45,5,28,1,1,1,8),_BsPortMirroringCtrlRowStatus_Type())
bsPortMirroringCtrlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlRowStatus.setStatus(_A)
_BsPortMirroringCtrlAllowTraffic_Type=TruthValue
_BsPortMirroringCtrlAllowTraffic_Object=MibTableColumn
bsPortMirroringCtrlAllowTraffic=_BsPortMirroringCtrlAllowTraffic_Object((1,3,6,1,4,1,45,5,28,1,1,1,9),_BsPortMirroringCtrlAllowTraffic_Type())
bsPortMirroringCtrlAllowTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlAllowTraffic.setStatus(_A)
class _BsPortMirroringCtrlRspanVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4094))
_BsPortMirroringCtrlRspanVlan_Type.__name__=_C
_BsPortMirroringCtrlRspanVlan_Object=MibTableColumn
bsPortMirroringCtrlRspanVlan=_BsPortMirroringCtrlRspanVlan_Object((1,3,6,1,4,1,45,5,28,1,1,1,10),_BsPortMirroringCtrlRspanVlan_Type())
bsPortMirroringCtrlRspanVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlRspanVlan.setStatus(_A)
class _BsPortMirroringCtrlMirrorVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BsPortMirroringCtrlMirrorVlan_Type.__name__=_C
_BsPortMirroringCtrlMirrorVlan_Object=MibTableColumn
bsPortMirroringCtrlMirrorVlan=_BsPortMirroringCtrlMirrorVlan_Object((1,3,6,1,4,1,45,5,28,1,1,1,11),_BsPortMirroringCtrlMirrorVlan_Type())
bsPortMirroringCtrlMirrorVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringCtrlMirrorVlan.setStatus(_A)
_BsPortMirroringRspanTable_Object=MibTable
bsPortMirroringRspanTable=_BsPortMirroringRspanTable_Object((1,3,6,1,4,1,45,5,28,1,2))
if mibBuilder.loadTexts:bsPortMirroringRspanTable.setStatus(_A)
_BsPortMirroringRspanEntry_Object=MibTableRow
bsPortMirroringRspanEntry=_BsPortMirroringRspanEntry_Object((1,3,6,1,4,1,45,5,28,1,2,1))
bsPortMirroringRspanEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:bsPortMirroringRspanEntry.setStatus(_A)
class _BsPortMirroringRspanInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BsPortMirroringRspanInstance_Type.__name__=_C
_BsPortMirroringRspanInstance_Object=MibTableColumn
bsPortMirroringRspanInstance=_BsPortMirroringRspanInstance_Object((1,3,6,1,4,1,45,5,28,1,2,1,1),_BsPortMirroringRspanInstance_Type())
bsPortMirroringRspanInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:bsPortMirroringRspanInstance.setStatus(_A)
_BsPortMirroringRspanMtp_Type=InterfaceIndex
_BsPortMirroringRspanMtp_Object=MibTableColumn
bsPortMirroringRspanMtp=_BsPortMirroringRspanMtp_Object((1,3,6,1,4,1,45,5,28,1,2,1,2),_BsPortMirroringRspanMtp_Type())
bsPortMirroringRspanMtp.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringRspanMtp.setStatus(_A)
class _BsPortMirroringRspanVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_BsPortMirroringRspanVlan_Type.__name__=_C
_BsPortMirroringRspanVlan_Object=MibTableColumn
bsPortMirroringRspanVlan=_BsPortMirroringRspanVlan_Object((1,3,6,1,4,1,45,5,28,1,2,1,3),_BsPortMirroringRspanVlan_Type())
bsPortMirroringRspanVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringRspanVlan.setStatus(_A)
_BsPortMirroringRspanRowStatus_Type=RowStatus
_BsPortMirroringRspanRowStatus_Object=MibTableColumn
bsPortMirroringRspanRowStatus=_BsPortMirroringRspanRowStatus_Object((1,3,6,1,4,1,45,5,28,1,2,1,4),_BsPortMirroringRspanRowStatus_Type())
bsPortMirroringRspanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsPortMirroringRspanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bayStackPortMirroringMib':bayStackPortMirroringMib,'bsPortMirroringNotifications':bsPortMirroringNotifications,'bsPortMirroringObjects':bsPortMirroringObjects,'bsPortMirroringCtrlTable':bsPortMirroringCtrlTable,'bsPortMirroringCtrlEntry':bsPortMirroringCtrlEntry,_F:bsPortMirroringCtrlInstance,'bsPortMirroringCtrlPortMode':bsPortMirroringCtrlPortMode,'bsPortMirroringCtrlMonitorPort':bsPortMirroringCtrlMonitorPort,'bsPortMirroringCtrlPortListX':bsPortMirroringCtrlPortListX,'bsPortMirroringCtrlPortListY':bsPortMirroringCtrlPortListY,'bsPortMirroringCtrlMacAddressA':bsPortMirroringCtrlMacAddressA,'bsPortMirroringCtrlMacAddressB':bsPortMirroringCtrlMacAddressB,'bsPortMirroringCtrlRowStatus':bsPortMirroringCtrlRowStatus,'bsPortMirroringCtrlAllowTraffic':bsPortMirroringCtrlAllowTraffic,'bsPortMirroringCtrlRspanVlan':bsPortMirroringCtrlRspanVlan,'bsPortMirroringCtrlMirrorVlan':bsPortMirroringCtrlMirrorVlan,'bsPortMirroringRspanTable':bsPortMirroringRspanTable,'bsPortMirroringRspanEntry':bsPortMirroringRspanEntry,_H:bsPortMirroringRspanInstance,'bsPortMirroringRspanMtp':bsPortMirroringRspanMtp,'bsPortMirroringRspanVlan':bsPortMirroringRspanVlan,'bsPortMirroringRspanRowStatus':bsPortMirroringRspanRowStatus})