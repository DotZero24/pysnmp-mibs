_O='rlDhcpApprovalActionMask'
_N='rlDhcpApprovalActionAddress'
_M='rlDhcpApprovalActionIfIndex'
_L='rlDhcpApprovalWaitingIfIndex'
_K='read-create'
_J='rlDhcpClActionIfIndex'
_I='DisplayString'
_H='SnmpAdminString'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-write'
_C='DLINK-3100-DHCPCL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlDhcpCl=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,76))
if mibBuilder.loadTexts:rlDhcpCl.setRevisions(('2007-01-02 00:00',))
_RlDhcpClActionTable_Object=MibTable
rlDhcpClActionTable=_RlDhcpClActionTable_Object((1,3,6,1,4,1,171,10,94,89,89,76,3))
if mibBuilder.loadTexts:rlDhcpClActionTable.setStatus(_A)
_RlDhcpClActionEntry_Object=MibTableRow
rlDhcpClActionEntry=_RlDhcpClActionEntry_Object((1,3,6,1,4,1,171,10,94,89,89,76,3,1))
rlDhcpClActionEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:rlDhcpClActionEntry.setStatus(_A)
_RlDhcpClActionIfIndex_Type=InterfaceIndex
_RlDhcpClActionIfIndex_Object=MibTableColumn
rlDhcpClActionIfIndex=_RlDhcpClActionIfIndex_Object((1,3,6,1,4,1,171,10,94,89,89,76,3,1,1),_RlDhcpClActionIfIndex_Type())
rlDhcpClActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClActionIfIndex.setStatus(_A)
_RlDhcpClActionStatus_Type=RowStatus
_RlDhcpClActionStatus_Object=MibTableColumn
rlDhcpClActionStatus=_RlDhcpClActionStatus_Object((1,3,6,1,4,1,171,10,94,89,89,76,3,1,2),_RlDhcpClActionStatus_Type())
rlDhcpClActionStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:rlDhcpClActionStatus.setStatus(_A)
class _RlDhcpClActionHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlDhcpClActionHostName_Type.__name__=_H
_RlDhcpClActionHostName_Object=MibTableColumn
rlDhcpClActionHostName=_RlDhcpClActionHostName_Object((1,3,6,1,4,1,171,10,94,89,89,76,3,1,3),_RlDhcpClActionHostName_Type())
rlDhcpClActionHostName.setMaxAccess(_K)
if mibBuilder.loadTexts:rlDhcpClActionHostName.setStatus(_A)
_RlDhcpApprovalEnabled_Type=TruthValue
_RlDhcpApprovalEnabled_Object=MibScalar
rlDhcpApprovalEnabled=_RlDhcpApprovalEnabled_Object((1,3,6,1,4,1,171,10,94,89,89,76,4),_RlDhcpApprovalEnabled_Type())
rlDhcpApprovalEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalEnabled.setStatus(_A)
_RlDhcpApprovalWaitingTable_Object=MibTable
rlDhcpApprovalWaitingTable=_RlDhcpApprovalWaitingTable_Object((1,3,6,1,4,1,171,10,94,89,89,76,5))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingTable.setStatus(_A)
_RlDhcpApprovalWaitingEntry_Object=MibTableRow
rlDhcpApprovalWaitingEntry=_RlDhcpApprovalWaitingEntry_Object((1,3,6,1,4,1,171,10,94,89,89,76,5,1))
rlDhcpApprovalWaitingEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingEntry.setStatus(_A)
_RlDhcpApprovalWaitingIfIndex_Type=InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object=MibTableColumn
rlDhcpApprovalWaitingIfIndex=_RlDhcpApprovalWaitingIfIndex_Object((1,3,6,1,4,1,171,10,94,89,89,76,5,1,1),_RlDhcpApprovalWaitingIfIndex_Type())
rlDhcpApprovalWaitingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingIfIndex.setStatus(_A)
_RlDhcpApprovalWaitingAddress_Type=IpAddress
_RlDhcpApprovalWaitingAddress_Object=MibTableColumn
rlDhcpApprovalWaitingAddress=_RlDhcpApprovalWaitingAddress_Object((1,3,6,1,4,1,171,10,94,89,89,76,5,1,2),_RlDhcpApprovalWaitingAddress_Type())
rlDhcpApprovalWaitingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingAddress.setStatus(_A)
_RlDhcpApprovalWaitingMask_Type=IpAddress
_RlDhcpApprovalWaitingMask_Object=MibTableColumn
rlDhcpApprovalWaitingMask=_RlDhcpApprovalWaitingMask_Object((1,3,6,1,4,1,171,10,94,89,89,76,5,1,3),_RlDhcpApprovalWaitingMask_Type())
rlDhcpApprovalWaitingMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingMask.setStatus(_A)
_RlDhcpApprovalWaitingGateway_Type=IpAddress
_RlDhcpApprovalWaitingGateway_Object=MibTableColumn
rlDhcpApprovalWaitingGateway=_RlDhcpApprovalWaitingGateway_Object((1,3,6,1,4,1,171,10,94,89,89,76,5,1,4),_RlDhcpApprovalWaitingGateway_Type())
rlDhcpApprovalWaitingGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingGateway.setStatus(_A)
_RlDhcpApprovalActionTable_Object=MibTable
rlDhcpApprovalActionTable=_RlDhcpApprovalActionTable_Object((1,3,6,1,4,1,171,10,94,89,89,76,6))
if mibBuilder.loadTexts:rlDhcpApprovalActionTable.setStatus(_A)
_RlDhcpApprovalActionEntry_Object=MibTableRow
rlDhcpApprovalActionEntry=_RlDhcpApprovalActionEntry_Object((1,3,6,1,4,1,171,10,94,89,89,76,6,1))
rlDhcpApprovalActionEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:rlDhcpApprovalActionEntry.setStatus(_A)
_RlDhcpApprovalActionIfIndex_Type=InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object=MibTableColumn
rlDhcpApprovalActionIfIndex=_RlDhcpApprovalActionIfIndex_Object((1,3,6,1,4,1,171,10,94,89,89,76,6,1,1),_RlDhcpApprovalActionIfIndex_Type())
rlDhcpApprovalActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionIfIndex.setStatus(_A)
_RlDhcpApprovalActionAddress_Type=IpAddress
_RlDhcpApprovalActionAddress_Object=MibTableColumn
rlDhcpApprovalActionAddress=_RlDhcpApprovalActionAddress_Object((1,3,6,1,4,1,171,10,94,89,89,76,6,1,2),_RlDhcpApprovalActionAddress_Type())
rlDhcpApprovalActionAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionAddress.setStatus(_A)
_RlDhcpApprovalActionMask_Type=IpAddress
_RlDhcpApprovalActionMask_Object=MibTableColumn
rlDhcpApprovalActionMask=_RlDhcpApprovalActionMask_Object((1,3,6,1,4,1,171,10,94,89,89,76,6,1,3),_RlDhcpApprovalActionMask_Type())
rlDhcpApprovalActionMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionMask.setStatus(_A)
_RlDhcpApprovalActionApprove_Type=TruthValue
_RlDhcpApprovalActionApprove_Object=MibTableColumn
rlDhcpApprovalActionApprove=_RlDhcpApprovalActionApprove_Object((1,3,6,1,4,1,171,10,94,89,89,76,6,1,4),_RlDhcpApprovalActionApprove_Type())
rlDhcpApprovalActionApprove.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpApprovalActionApprove.setStatus(_A)
_RlDhcpClCommandTable_Object=MibTable
rlDhcpClCommandTable=_RlDhcpClCommandTable_Object((1,3,6,1,4,1,171,10,94,89,89,76,7))
if mibBuilder.loadTexts:rlDhcpClCommandTable.setStatus(_A)
_RlDhcpClCommandEntry_Object=MibTableRow
rlDhcpClCommandEntry=_RlDhcpClCommandEntry_Object((1,3,6,1,4,1,171,10,94,89,89,76,7,1))
rlDhcpClCommandEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rlDhcpClCommandEntry.setStatus(_A)
class _RlDhcpClCommandAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('renew',1),('renewForceAutoconfig',2)))
_RlDhcpClCommandAction_Type.__name__=_E
_RlDhcpClCommandAction_Object=MibTableColumn
rlDhcpClCommandAction=_RlDhcpClCommandAction_Object((1,3,6,1,4,1,171,10,94,89,89,76,7,1,2),_RlDhcpClCommandAction_Type())
rlDhcpClCommandAction.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpClCommandAction.setStatus(_A)
class _RlDhcpClConfigurationFileName_Type(DisplayString):defaultValue=OctetString('')
_RlDhcpClConfigurationFileName_Type.__name__=_I
_RlDhcpClConfigurationFileName_Object=MibScalar
rlDhcpClConfigurationFileName=_RlDhcpClConfigurationFileName_Object((1,3,6,1,4,1,171,10,94,89,89,76,8),_RlDhcpClConfigurationFileName_Type())
rlDhcpClConfigurationFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpClConfigurationFileName.setStatus(_A)
class _RlDhcpClOption67Enable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RlDhcpClOption67Enable_Type.__name__=_E
_RlDhcpClOption67Enable_Object=MibScalar
rlDhcpClOption67Enable=_RlDhcpClOption67Enable_Object((1,3,6,1,4,1,171,10,94,89,89,76,9),_RlDhcpClOption67Enable_Type())
rlDhcpClOption67Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlDhcpClOption67Enable.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rlDhcpCl':rlDhcpCl,'rlDhcpClActionTable':rlDhcpClActionTable,'rlDhcpClActionEntry':rlDhcpClActionEntry,_J:rlDhcpClActionIfIndex,'rlDhcpClActionStatus':rlDhcpClActionStatus,'rlDhcpClActionHostName':rlDhcpClActionHostName,'rlDhcpApprovalEnabled':rlDhcpApprovalEnabled,'rlDhcpApprovalWaitingTable':rlDhcpApprovalWaitingTable,'rlDhcpApprovalWaitingEntry':rlDhcpApprovalWaitingEntry,_L:rlDhcpApprovalWaitingIfIndex,'rlDhcpApprovalWaitingAddress':rlDhcpApprovalWaitingAddress,'rlDhcpApprovalWaitingMask':rlDhcpApprovalWaitingMask,'rlDhcpApprovalWaitingGateway':rlDhcpApprovalWaitingGateway,'rlDhcpApprovalActionTable':rlDhcpApprovalActionTable,'rlDhcpApprovalActionEntry':rlDhcpApprovalActionEntry,_M:rlDhcpApprovalActionIfIndex,_N:rlDhcpApprovalActionAddress,_O:rlDhcpApprovalActionMask,'rlDhcpApprovalActionApprove':rlDhcpApprovalActionApprove,'rlDhcpClCommandTable':rlDhcpClCommandTable,'rlDhcpClCommandEntry':rlDhcpClCommandEntry,'rlDhcpClCommandAction':rlDhcpClCommandAction,'rlDhcpClConfigurationFileName':rlDhcpClConfigurationFileName,'rlDhcpClOption67Enable':rlDhcpClOption67Enable})