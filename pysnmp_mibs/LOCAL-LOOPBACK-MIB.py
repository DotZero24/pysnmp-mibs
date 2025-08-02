_G='read-write'
_F='other'
_E='swLocalLoopbackPort'
_D='LOCAL-LOOPBACK-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swLocalLoopbackMIB=ModuleIdentity((1,3,6,1,4,1,171,12,67))
_SwLocalLoopbackCtrl_ObjectIdentity=ObjectIdentity
swLocalLoopbackCtrl=_SwLocalLoopbackCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,67,1))
_SwLocalLoopbackInfo_ObjectIdentity=ObjectIdentity
swLocalLoopbackInfo=_SwLocalLoopbackInfo_ObjectIdentity((1,3,6,1,4,1,171,12,67,2))
_SwLocalLoopbackMgmt_ObjectIdentity=ObjectIdentity
swLocalLoopbackMgmt=_SwLocalLoopbackMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,67,3))
_SwLocalLoopbackConfigTable_Object=MibTable
swLocalLoopbackConfigTable=_SwLocalLoopbackConfigTable_Object((1,3,6,1,4,1,171,12,67,3,1))
if mibBuilder.loadTexts:swLocalLoopbackConfigTable.setStatus(_A)
_SwLocalLoopbackConfigEntry_Object=MibTableRow
swLocalLoopbackConfigEntry=_SwLocalLoopbackConfigEntry_Object((1,3,6,1,4,1,171,12,67,3,1,1))
swLocalLoopbackConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swLocalLoopbackConfigEntry.setStatus(_A)
_SwLocalLoopbackPort_Type=Integer32
_SwLocalLoopbackPort_Object=MibTableColumn
swLocalLoopbackPort=_SwLocalLoopbackPort_Object((1,3,6,1,4,1,171,12,67,3,1,1,1),_SwLocalLoopbackPort_Type())
swLocalLoopbackPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopbackPort.setStatus(_A)
class _SwLocalLoopbackMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('internal',2),('external',3)))
_SwLocalLoopbackMethod_Type.__name__=_C
_SwLocalLoopbackMethod_Object=MibTableColumn
swLocalLoopbackMethod=_SwLocalLoopbackMethod_Object((1,3,6,1,4,1,171,12,67,3,1,1,2),_SwLocalLoopbackMethod_Type())
swLocalLoopbackMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:swLocalLoopbackMethod.setStatus(_A)
class _SwLocalLoopbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('mac',2),('phy-copper',3),('phy-fiber',4)))
_SwLocalLoopbackMode_Type.__name__=_C
_SwLocalLoopbackMode_Object=MibTableColumn
swLocalLoopbackMode=_SwLocalLoopbackMode_Object((1,3,6,1,4,1,171,12,67,3,1,1,3),_SwLocalLoopbackMode_Type())
swLocalLoopbackMode.setMaxAccess(_G)
if mibBuilder.loadTexts:swLocalLoopbackMode.setStatus(_A)
class _SwLocalLoopbackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwLocalLoopbackState_Type.__name__=_C
_SwLocalLoopbackState_Object=MibTableColumn
swLocalLoopbackState=_SwLocalLoopbackState_Object((1,3,6,1,4,1,171,12,67,3,1,1,4),_SwLocalLoopbackState_Type())
swLocalLoopbackState.setMaxAccess(_G)
if mibBuilder.loadTexts:swLocalLoopbackState.setStatus(_A)
_SwLocalLoopbackResultTable_Object=MibTable
swLocalLoopbackResultTable=_SwLocalLoopbackResultTable_Object((1,3,6,1,4,1,171,12,67,3,2))
if mibBuilder.loadTexts:swLocalLoopbackResultTable.setStatus(_A)
_SwLocalLoopbackResultEntry_Object=MibTableRow
swLocalLoopbackResultEntry=_SwLocalLoopbackResultEntry_Object((1,3,6,1,4,1,171,12,67,3,2,1))
swLocalLoopbackResultEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swLocalLoopbackResultEntry.setStatus(_A)
_SwLocalLoopback64Tx_Type=Counter32
_SwLocalLoopback64Tx_Object=MibTableColumn
swLocalLoopback64Tx=_SwLocalLoopback64Tx_Object((1,3,6,1,4,1,171,12,67,3,2,1,1),_SwLocalLoopback64Tx_Type())
swLocalLoopback64Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback64Tx.setStatus(_A)
_SwLocalLoopback64Rx_Type=Counter32
_SwLocalLoopback64Rx_Object=MibTableColumn
swLocalLoopback64Rx=_SwLocalLoopback64Rx_Object((1,3,6,1,4,1,171,12,67,3,2,1,2),_SwLocalLoopback64Rx_Type())
swLocalLoopback64Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback64Rx.setStatus(_A)
_SwLocalLoopback512Tx_Type=Counter32
_SwLocalLoopback512Tx_Object=MibTableColumn
swLocalLoopback512Tx=_SwLocalLoopback512Tx_Object((1,3,6,1,4,1,171,12,67,3,2,1,3),_SwLocalLoopback512Tx_Type())
swLocalLoopback512Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback512Tx.setStatus(_A)
_SwLocalLoopback512Rx_Type=Counter32
_SwLocalLoopback512Rx_Object=MibTableColumn
swLocalLoopback512Rx=_SwLocalLoopback512Rx_Object((1,3,6,1,4,1,171,12,67,3,2,1,4),_SwLocalLoopback512Rx_Type())
swLocalLoopback512Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback512Rx.setStatus(_A)
_SwLocalLoopback1024Tx_Type=Counter32
_SwLocalLoopback1024Tx_Object=MibTableColumn
swLocalLoopback1024Tx=_SwLocalLoopback1024Tx_Object((1,3,6,1,4,1,171,12,67,3,2,1,5),_SwLocalLoopback1024Tx_Type())
swLocalLoopback1024Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback1024Tx.setStatus(_A)
_SwLocalLoopback1024Rx_Type=Counter32
_SwLocalLoopback1024Rx_Object=MibTableColumn
swLocalLoopback1024Rx=_SwLocalLoopback1024Rx_Object((1,3,6,1,4,1,171,12,67,3,2,1,6),_SwLocalLoopback1024Rx_Type())
swLocalLoopback1024Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback1024Rx.setStatus(_A)
_SwLocalLoopback1536Tx_Type=Counter32
_SwLocalLoopback1536Tx_Object=MibTableColumn
swLocalLoopback1536Tx=_SwLocalLoopback1536Tx_Object((1,3,6,1,4,1,171,12,67,3,2,1,7),_SwLocalLoopback1536Tx_Type())
swLocalLoopback1536Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback1536Tx.setStatus(_A)
_SwLocalLoopback1536Rx_Type=Counter32
_SwLocalLoopback1536Rx_Object=MibTableColumn
swLocalLoopback1536Rx=_SwLocalLoopback1536Rx_Object((1,3,6,1,4,1,171,12,67,3,2,1,8),_SwLocalLoopback1536Rx_Type())
swLocalLoopback1536Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopback1536Rx.setStatus(_A)
class _SwLocalLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('success',2),('fail',3)))
_SwLocalLoopbackStatus_Type.__name__=_C
_SwLocalLoopbackStatus_Object=MibTableColumn
swLocalLoopbackStatus=_SwLocalLoopbackStatus_Object((1,3,6,1,4,1,171,12,67,3,2,1,9),_SwLocalLoopbackStatus_Type())
swLocalLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swLocalLoopbackStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swLocalLoopbackMIB':swLocalLoopbackMIB,'swLocalLoopbackCtrl':swLocalLoopbackCtrl,'swLocalLoopbackInfo':swLocalLoopbackInfo,'swLocalLoopbackMgmt':swLocalLoopbackMgmt,'swLocalLoopbackConfigTable':swLocalLoopbackConfigTable,'swLocalLoopbackConfigEntry':swLocalLoopbackConfigEntry,_E:swLocalLoopbackPort,'swLocalLoopbackMethod':swLocalLoopbackMethod,'swLocalLoopbackMode':swLocalLoopbackMode,'swLocalLoopbackState':swLocalLoopbackState,'swLocalLoopbackResultTable':swLocalLoopbackResultTable,'swLocalLoopbackResultEntry':swLocalLoopbackResultEntry,'swLocalLoopback64Tx':swLocalLoopback64Tx,'swLocalLoopback64Rx':swLocalLoopback64Rx,'swLocalLoopback512Tx':swLocalLoopback512Tx,'swLocalLoopback512Rx':swLocalLoopback512Rx,'swLocalLoopback1024Tx':swLocalLoopback1024Tx,'swLocalLoopback1024Rx':swLocalLoopback1024Rx,'swLocalLoopback1536Tx':swLocalLoopback1536Tx,'swLocalLoopback1536Rx':swLocalLoopback1536Rx,'swLocalLoopbackStatus':swLocalLoopbackStatus})