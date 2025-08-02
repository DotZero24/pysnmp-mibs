_O='zxAnAtmPerfIfIndex'
_N='zxAnAtmPvcVci'
_M='zxAnAtmPvcVpi'
_L='zxAnAtmIfIndex'
_K='read-create'
_J='zxAnAtmVcxWanSidePvcId'
_I='zxAnAtmVcxWanSideIfIndex'
_H='zxAnAtmVcxUserSidePvcId'
_G='zxAnAtmVcxUserSideIfIndex'
_F='RowStatus'
_E='Integer32'
_D='read-only'
_C='not-accessible'
_B='ZTE-AN-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_F,'TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnAtmMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,57))
_ZxAnAtmVcxObjects_ObjectIdentity=ObjectIdentity
zxAnAtmVcxObjects=_ZxAnAtmVcxObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,57,1))
_ZxAnAtmVcxTable_Object=MibTable
zxAnAtmVcxTable=_ZxAnAtmVcxTable_Object((1,3,6,1,4,1,3902,1015,57,1,1))
if mibBuilder.loadTexts:zxAnAtmVcxTable.setStatus(_A)
_ZxAnAtmVcxEntry_Object=MibTableRow
zxAnAtmVcxEntry=_ZxAnAtmVcxEntry_Object((1,3,6,1,4,1,3902,1015,57,1,1,1))
zxAnAtmVcxEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zxAnAtmVcxEntry.setStatus(_A)
_ZxAnAtmVcxUserSideIfIndex_Type=ZxAnIfindex
_ZxAnAtmVcxUserSideIfIndex_Object=MibTableColumn
zxAnAtmVcxUserSideIfIndex=_ZxAnAtmVcxUserSideIfIndex_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,1),_ZxAnAtmVcxUserSideIfIndex_Type())
zxAnAtmVcxUserSideIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmVcxUserSideIfIndex.setStatus(_A)
_ZxAnAtmVcxUserSidePvcId_Type=Integer32
_ZxAnAtmVcxUserSidePvcId_Object=MibTableColumn
zxAnAtmVcxUserSidePvcId=_ZxAnAtmVcxUserSidePvcId_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,2),_ZxAnAtmVcxUserSidePvcId_Type())
zxAnAtmVcxUserSidePvcId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmVcxUserSidePvcId.setStatus(_A)
_ZxAnAtmVcxWanSideIfIndex_Type=ZxAnIfindex
_ZxAnAtmVcxWanSideIfIndex_Object=MibTableColumn
zxAnAtmVcxWanSideIfIndex=_ZxAnAtmVcxWanSideIfIndex_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,3),_ZxAnAtmVcxWanSideIfIndex_Type())
zxAnAtmVcxWanSideIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmVcxWanSideIfIndex.setStatus(_A)
_ZxAnAtmVcxWanSidePvcId_Type=Integer32
_ZxAnAtmVcxWanSidePvcId_Object=MibTableColumn
zxAnAtmVcxWanSidePvcId=_ZxAnAtmVcxWanSidePvcId_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,4),_ZxAnAtmVcxWanSidePvcId_Type())
zxAnAtmVcxWanSidePvcId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmVcxWanSidePvcId.setStatus(_A)
_ZxAnAtmVcxUserSideVpi_Type=Integer32
_ZxAnAtmVcxUserSideVpi_Object=MibTableColumn
zxAnAtmVcxUserSideVpi=_ZxAnAtmVcxUserSideVpi_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,5),_ZxAnAtmVcxUserSideVpi_Type())
zxAnAtmVcxUserSideVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmVcxUserSideVpi.setStatus(_A)
_ZxAnAtmVcxUserSideVci_Type=Integer32
_ZxAnAtmVcxUserSideVci_Object=MibTableColumn
zxAnAtmVcxUserSideVci=_ZxAnAtmVcxUserSideVci_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,6),_ZxAnAtmVcxUserSideVci_Type())
zxAnAtmVcxUserSideVci.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmVcxUserSideVci.setStatus(_A)
_ZxAnAtmVcxWanSideVpi_Type=Integer32
_ZxAnAtmVcxWanSideVpi_Object=MibTableColumn
zxAnAtmVcxWanSideVpi=_ZxAnAtmVcxWanSideVpi_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,7),_ZxAnAtmVcxWanSideVpi_Type())
zxAnAtmVcxWanSideVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmVcxWanSideVpi.setStatus(_A)
_ZxAnAtmVcxWanSideVci_Type=Integer32
_ZxAnAtmVcxWanSideVci_Object=MibTableColumn
zxAnAtmVcxWanSideVci=_ZxAnAtmVcxWanSideVci_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,8),_ZxAnAtmVcxWanSideVci_Type())
zxAnAtmVcxWanSideVci.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmVcxWanSideVci.setStatus(_A)
class _ZxAnAtmVcxRowStatus_Type(RowStatus):defaultValue=5
_ZxAnAtmVcxRowStatus_Type.__name__=_F
_ZxAnAtmVcxRowStatus_Object=MibTableColumn
zxAnAtmVcxRowStatus=_ZxAnAtmVcxRowStatus_Object((1,3,6,1,4,1,3902,1015,57,1,1,1,50),_ZxAnAtmVcxRowStatus_Type())
zxAnAtmVcxRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnAtmVcxRowStatus.setStatus(_A)
_ZxAnAtmPvcMappingIdTable_Object=MibTable
zxAnAtmPvcMappingIdTable=_ZxAnAtmPvcMappingIdTable_Object((1,3,6,1,4,1,3902,1015,57,1,3))
if mibBuilder.loadTexts:zxAnAtmPvcMappingIdTable.setStatus(_A)
_ZxAnAtmPvcMappingIdEntry_Object=MibTableRow
zxAnAtmPvcMappingIdEntry=_ZxAnAtmPvcMappingIdEntry_Object((1,3,6,1,4,1,3902,1015,57,1,3,1))
zxAnAtmPvcMappingIdEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:zxAnAtmPvcMappingIdEntry.setStatus(_A)
_ZxAnAtmIfIndex_Type=ZxAnIfindex
_ZxAnAtmIfIndex_Object=MibTableColumn
zxAnAtmIfIndex=_ZxAnAtmIfIndex_Object((1,3,6,1,4,1,3902,1015,57,1,3,1,1),_ZxAnAtmIfIndex_Type())
zxAnAtmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmIfIndex.setStatus(_A)
class _ZxAnAtmPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnAtmPvcVpi_Type.__name__=_E
_ZxAnAtmPvcVpi_Object=MibTableColumn
zxAnAtmPvcVpi=_ZxAnAtmPvcVpi_Object((1,3,6,1,4,1,3902,1015,57,1,3,1,2),_ZxAnAtmPvcVpi_Type())
zxAnAtmPvcVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmPvcVpi.setStatus(_A)
class _ZxAnAtmPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnAtmPvcVci_Type.__name__=_E
_ZxAnAtmPvcVci_Object=MibTableColumn
zxAnAtmPvcVci=_ZxAnAtmPvcVci_Object((1,3,6,1,4,1,3902,1015,57,1,3,1,3),_ZxAnAtmPvcVci_Type())
zxAnAtmPvcVci.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmPvcVci.setStatus(_A)
_ZxAnAtmPvcId_Type=Integer32
_ZxAnAtmPvcId_Object=MibTableColumn
zxAnAtmPvcId=_ZxAnAtmPvcId_Object((1,3,6,1,4,1,3902,1015,57,1,3,1,4),_ZxAnAtmPvcId_Type())
zxAnAtmPvcId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnAtmPvcId.setStatus(_A)
_ZxAnAtmPerfObjects_ObjectIdentity=ObjectIdentity
zxAnAtmPerfObjects=_ZxAnAtmPerfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,57,2))
_ZxAnAtmPerfTable_Object=MibTable
zxAnAtmPerfTable=_ZxAnAtmPerfTable_Object((1,3,6,1,4,1,3902,1015,57,2,1))
if mibBuilder.loadTexts:zxAnAtmPerfTable.setStatus(_A)
_ZxAnAtmPerfEntry_Object=MibTableRow
zxAnAtmPerfEntry=_ZxAnAtmPerfEntry_Object((1,3,6,1,4,1,3902,1015,57,2,1,1))
zxAnAtmPerfEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:zxAnAtmPerfEntry.setStatus(_A)
_ZxAnAtmPerfIfIndex_Type=ZxAnIfindex
_ZxAnAtmPerfIfIndex_Object=MibTableColumn
zxAnAtmPerfIfIndex=_ZxAnAtmPerfIfIndex_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,1),_ZxAnAtmPerfIfIndex_Type())
zxAnAtmPerfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAtmPerfIfIndex.setStatus(_A)
_ZxAnAtmReceiveCell_Type=Counter64
_ZxAnAtmReceiveCell_Object=MibTableColumn
zxAnAtmReceiveCell=_ZxAnAtmReceiveCell_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,2),_ZxAnAtmReceiveCell_Type())
zxAnAtmReceiveCell.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmReceiveCell.setStatus(_A)
_ZxAnAtmTransmitCell_Type=Counter64
_ZxAnAtmTransmitCell_Object=MibTableColumn
zxAnAtmTransmitCell=_ZxAnAtmTransmitCell_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,3),_ZxAnAtmTransmitCell_Type())
zxAnAtmTransmitCell.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmTransmitCell.setStatus(_A)
_ZxAnAtmDiscardedCell_Type=Counter64
_ZxAnAtmDiscardedCell_Object=MibTableColumn
zxAnAtmDiscardedCell=_ZxAnAtmDiscardedCell_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,4),_ZxAnAtmDiscardedCell_Type())
zxAnAtmDiscardedCell.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmDiscardedCell.setStatus(_A)
_ZxAnAtmContinuityCell_Type=Counter64
_ZxAnAtmContinuityCell_Object=MibTableColumn
zxAnAtmContinuityCell=_ZxAnAtmContinuityCell_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,5),_ZxAnAtmContinuityCell_Type())
zxAnAtmContinuityCell.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAtmContinuityCell.setStatus(_A)
class _ZxATMStatCounterAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('resetCounter',3)))
_ZxATMStatCounterAdminStatus_Type.__name__=_E
_ZxATMStatCounterAdminStatus_Object=MibTableColumn
zxATMStatCounterAdminStatus=_ZxATMStatCounterAdminStatus_Object((1,3,6,1,4,1,3902,1015,57,2,1,1,6),_ZxATMStatCounterAdminStatus_Type())
zxATMStatCounterAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxATMStatCounterAdminStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnAtmMib':zxAnAtmMib,'zxAnAtmVcxObjects':zxAnAtmVcxObjects,'zxAnAtmVcxTable':zxAnAtmVcxTable,'zxAnAtmVcxEntry':zxAnAtmVcxEntry,_G:zxAnAtmVcxUserSideIfIndex,_H:zxAnAtmVcxUserSidePvcId,_I:zxAnAtmVcxWanSideIfIndex,_J:zxAnAtmVcxWanSidePvcId,'zxAnAtmVcxUserSideVpi':zxAnAtmVcxUserSideVpi,'zxAnAtmVcxUserSideVci':zxAnAtmVcxUserSideVci,'zxAnAtmVcxWanSideVpi':zxAnAtmVcxWanSideVpi,'zxAnAtmVcxWanSideVci':zxAnAtmVcxWanSideVci,'zxAnAtmVcxRowStatus':zxAnAtmVcxRowStatus,'zxAnAtmPvcMappingIdTable':zxAnAtmPvcMappingIdTable,'zxAnAtmPvcMappingIdEntry':zxAnAtmPvcMappingIdEntry,_L:zxAnAtmIfIndex,_M:zxAnAtmPvcVpi,_N:zxAnAtmPvcVci,'zxAnAtmPvcId':zxAnAtmPvcId,'zxAnAtmPerfObjects':zxAnAtmPerfObjects,'zxAnAtmPerfTable':zxAnAtmPerfTable,'zxAnAtmPerfEntry':zxAnAtmPerfEntry,_O:zxAnAtmPerfIfIndex,'zxAnAtmReceiveCell':zxAnAtmReceiveCell,'zxAnAtmTransmitCell':zxAnAtmTransmitCell,'zxAnAtmDiscardedCell':zxAnAtmDiscardedCell,'zxAnAtmContinuityCell':zxAnAtmContinuityCell,'zxATMStatCounterAdminStatus':zxATMStatCounterAdminStatus})