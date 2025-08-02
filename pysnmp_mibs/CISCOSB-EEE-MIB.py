_G='read-write'
_F='TruthValue'
_E='ifIndex'
_D='IF-MIB'
_C='uSec'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ifIndex,ifOperStatus=mibBuilder.importSymbols(_D,_E,'ifOperStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
rlEee=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,149))
if mibBuilder.loadTexts:rlEee.setRevisions(('2010-05-15 00:00',))
class _RlEeeEnable_Type(TruthValue):defaultValue=2
_RlEeeEnable_Type.__name__=_F
_RlEeeEnable_Object=MibScalar
rlEeeEnable=_RlEeeEnable_Object((1,3,6,1,4,1,9,6,1,101,149,1),_RlEeeEnable_Type())
rlEeeEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:rlEeeEnable.setStatus(_A)
_RlEeePortTable_Object=MibTable
rlEeePortTable=_RlEeePortTable_Object((1,3,6,1,4,1,9,6,1,101,149,2))
if mibBuilder.loadTexts:rlEeePortTable.setStatus(_A)
_RlEeePortEntry_Object=MibTableRow
rlEeePortEntry=_RlEeePortEntry_Object((1,3,6,1,4,1,9,6,1,101,149,2,1))
rlEeePortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlEeePortEntry.setStatus(_A)
class _RlEeePortAdminStatus_Type(TruthValue):defaultValue=2
_RlEeePortAdminStatus_Type.__name__=_F
_RlEeePortAdminStatus_Object=MibTableColumn
rlEeePortAdminStatus=_RlEeePortAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,149,2,1,1),_RlEeePortAdminStatus_Type())
rlEeePortAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlEeePortAdminStatus.setStatus(_A)
class _RlEeePortSupported_Type(Bits):namedValues=NamedValues(*(('rlEeePortSupported10M',0),('rlEeePortSupported100M',1),('rlEeePortSupported1G',2),('rlEeePortSupported10G',3),('rlEeePortSupported2500M',4),('rlEeePortSupported5G',5)))
_RlEeePortSupported_Type.__name__='Bits'
_RlEeePortSupported_Object=MibTableColumn
rlEeePortSupported=_RlEeePortSupported_Object((1,3,6,1,4,1,9,6,1,101,149,2,1,2),_RlEeePortSupported_Type())
rlEeePortSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortSupported.setStatus(_A)
_RlEeePortRemoteStatus_Type=TruthValue
_RlEeePortRemoteStatus_Object=MibTableColumn
rlEeePortRemoteStatus=_RlEeePortRemoteStatus_Object((1,3,6,1,4,1,9,6,1,101,149,2,1,3),_RlEeePortRemoteStatus_Type())
rlEeePortRemoteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortRemoteStatus.setStatus(_A)
_RlEeePortOperStatus_Type=TruthValue
_RlEeePortOperStatus_Object=MibTableColumn
rlEeePortOperStatus=_RlEeePortOperStatus_Object((1,3,6,1,4,1,9,6,1,101,149,2,1,4),_RlEeePortOperStatus_Type())
rlEeePortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortOperStatus.setStatus(_A)
_RlEeePortLldpTable_Object=MibTable
rlEeePortLldpTable=_RlEeePortLldpTable_Object((1,3,6,1,4,1,9,6,1,101,149,3))
if mibBuilder.loadTexts:rlEeePortLldpTable.setStatus(_A)
_RlEeePortLldpEntry_Object=MibTableRow
rlEeePortLldpEntry=_RlEeePortLldpEntry_Object((1,3,6,1,4,1,9,6,1,101,149,3,1))
rlEeePortLldpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlEeePortLldpEntry.setStatus(_A)
class _RlEeePortLldpAdminStatus_Type(TruthValue):defaultValue=2
_RlEeePortLldpAdminStatus_Type.__name__=_F
_RlEeePortLldpAdminStatus_Object=MibTableColumn
rlEeePortLldpAdminStatus=_RlEeePortLldpAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,149,3,1,1),_RlEeePortLldpAdminStatus_Type())
rlEeePortLldpAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlEeePortLldpAdminStatus.setStatus(_A)
_RlEeePortLldpOperStatus_Type=TruthValue
_RlEeePortLldpOperStatus_Object=MibTableColumn
rlEeePortLldpOperStatus=_RlEeePortLldpOperStatus_Object((1,3,6,1,4,1,9,6,1,101,149,3,1,2),_RlEeePortLldpOperStatus_Type())
rlEeePortLldpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpOperStatus.setStatus(_A)
_RlEeePortLldpLocalTable_Object=MibTable
rlEeePortLldpLocalTable=_RlEeePortLldpLocalTable_Object((1,3,6,1,4,1,9,6,1,101,149,4))
if mibBuilder.loadTexts:rlEeePortLldpLocalTable.setStatus(_A)
_RlEeePortLldpLocalEntry_Object=MibTableRow
rlEeePortLldpLocalEntry=_RlEeePortLldpLocalEntry_Object((1,3,6,1,4,1,9,6,1,101,149,4,1))
rlEeePortLldpLocalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlEeePortLldpLocalEntry.setStatus(_A)
_RlEeePortLldpLocalResolvedTx_Type=Unsigned32
_RlEeePortLldpLocalResolvedTx_Object=MibTableColumn
rlEeePortLldpLocalResolvedTx=_RlEeePortLldpLocalResolvedTx_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,1),_RlEeePortLldpLocalResolvedTx_Type())
rlEeePortLldpLocalResolvedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalResolvedTx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalResolvedTx.setUnits(_C)
_RlEeePortLldpLocalTx_Type=Unsigned32
_RlEeePortLldpLocalTx_Object=MibTableColumn
rlEeePortLldpLocalTx=_RlEeePortLldpLocalTx_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,2),_RlEeePortLldpLocalTx_Type())
rlEeePortLldpLocalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalTx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalTx.setUnits(_C)
_RlEeePortLldpLocalTxEcho_Type=Unsigned32
_RlEeePortLldpLocalTxEcho_Object=MibTableColumn
rlEeePortLldpLocalTxEcho=_RlEeePortLldpLocalTxEcho_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,3),_RlEeePortLldpLocalTxEcho_Type())
rlEeePortLldpLocalTxEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalTxEcho.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalTxEcho.setUnits(_C)
_RlEeePortLldpLocalResolvedRx_Type=Unsigned32
_RlEeePortLldpLocalResolvedRx_Object=MibTableColumn
rlEeePortLldpLocalResolvedRx=_RlEeePortLldpLocalResolvedRx_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,4),_RlEeePortLldpLocalResolvedRx_Type())
rlEeePortLldpLocalResolvedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalResolvedRx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalResolvedRx.setUnits(_C)
_RlEeePortLldpLocalRx_Type=Unsigned32
_RlEeePortLldpLocalRx_Object=MibTableColumn
rlEeePortLldpLocalRx=_RlEeePortLldpLocalRx_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,5),_RlEeePortLldpLocalRx_Type())
rlEeePortLldpLocalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalRx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalRx.setUnits(_C)
_RlEeePortLldpLocalRxEcho_Type=Unsigned32
_RlEeePortLldpLocalRxEcho_Object=MibTableColumn
rlEeePortLldpLocalRxEcho=_RlEeePortLldpLocalRxEcho_Object((1,3,6,1,4,1,9,6,1,101,149,4,1,6),_RlEeePortLldpLocalRxEcho_Type())
rlEeePortLldpLocalRxEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpLocalRxEcho.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpLocalRxEcho.setUnits(_C)
_RlEeePortLldpRemoteTable_Object=MibTable
rlEeePortLldpRemoteTable=_RlEeePortLldpRemoteTable_Object((1,3,6,1,4,1,9,6,1,101,149,5))
if mibBuilder.loadTexts:rlEeePortLldpRemoteTable.setStatus(_A)
_RlEeePortLldpRemoteEntry_Object=MibTableRow
rlEeePortLldpRemoteEntry=_RlEeePortLldpRemoteEntry_Object((1,3,6,1,4,1,9,6,1,101,149,5,1))
rlEeePortLldpRemoteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlEeePortLldpRemoteEntry.setStatus(_A)
_RlEeePortLldpRemoteTx_Type=Unsigned32
_RlEeePortLldpRemoteTx_Object=MibTableColumn
rlEeePortLldpRemoteTx=_RlEeePortLldpRemoteTx_Object((1,3,6,1,4,1,9,6,1,101,149,5,1,1),_RlEeePortLldpRemoteTx_Type())
rlEeePortLldpRemoteTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpRemoteTx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpRemoteTx.setUnits(_C)
_RlEeePortLldpRemoteRx_Type=Unsigned32
_RlEeePortLldpRemoteRx_Object=MibTableColumn
rlEeePortLldpRemoteRx=_RlEeePortLldpRemoteRx_Object((1,3,6,1,4,1,9,6,1,101,149,5,1,2),_RlEeePortLldpRemoteRx_Type())
rlEeePortLldpRemoteRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpRemoteRx.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpRemoteRx.setUnits(_C)
_RlEeePortLldpRemoteTxEcho_Type=Unsigned32
_RlEeePortLldpRemoteTxEcho_Object=MibTableColumn
rlEeePortLldpRemoteTxEcho=_RlEeePortLldpRemoteTxEcho_Object((1,3,6,1,4,1,9,6,1,101,149,5,1,3),_RlEeePortLldpRemoteTxEcho_Type())
rlEeePortLldpRemoteTxEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpRemoteTxEcho.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpRemoteTxEcho.setUnits(_C)
_RlEeePortLldpRemoteRxEcho_Type=Unsigned32
_RlEeePortLldpRemoteRxEcho_Object=MibTableColumn
rlEeePortLldpRemoteRxEcho=_RlEeePortLldpRemoteRxEcho_Object((1,3,6,1,4,1,9,6,1,101,149,5,1,4),_RlEeePortLldpRemoteRxEcho_Type())
rlEeePortLldpRemoteRxEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:rlEeePortLldpRemoteRxEcho.setStatus(_A)
if mibBuilder.loadTexts:rlEeePortLldpRemoteRxEcho.setUnits(_C)
mibBuilder.exportSymbols('CISCOSB-EEE-MIB',**{'rlEee':rlEee,'rlEeeEnable':rlEeeEnable,'rlEeePortTable':rlEeePortTable,'rlEeePortEntry':rlEeePortEntry,'rlEeePortAdminStatus':rlEeePortAdminStatus,'rlEeePortSupported':rlEeePortSupported,'rlEeePortRemoteStatus':rlEeePortRemoteStatus,'rlEeePortOperStatus':rlEeePortOperStatus,'rlEeePortLldpTable':rlEeePortLldpTable,'rlEeePortLldpEntry':rlEeePortLldpEntry,'rlEeePortLldpAdminStatus':rlEeePortLldpAdminStatus,'rlEeePortLldpOperStatus':rlEeePortLldpOperStatus,'rlEeePortLldpLocalTable':rlEeePortLldpLocalTable,'rlEeePortLldpLocalEntry':rlEeePortLldpLocalEntry,'rlEeePortLldpLocalResolvedTx':rlEeePortLldpLocalResolvedTx,'rlEeePortLldpLocalTx':rlEeePortLldpLocalTx,'rlEeePortLldpLocalTxEcho':rlEeePortLldpLocalTxEcho,'rlEeePortLldpLocalResolvedRx':rlEeePortLldpLocalResolvedRx,'rlEeePortLldpLocalRx':rlEeePortLldpLocalRx,'rlEeePortLldpLocalRxEcho':rlEeePortLldpLocalRxEcho,'rlEeePortLldpRemoteTable':rlEeePortLldpRemoteTable,'rlEeePortLldpRemoteEntry':rlEeePortLldpRemoteEntry,'rlEeePortLldpRemoteTx':rlEeePortLldpRemoteTx,'rlEeePortLldpRemoteRx':rlEeePortLldpRemoteRx,'rlEeePortLldpRemoteTxEcho':rlEeePortLldpRemoteTxEcho,'rlEeePortLldpRemoteRxEcho':rlEeePortLldpRemoteRxEcho})