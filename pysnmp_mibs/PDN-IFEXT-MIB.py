_J='pdnIfExtTestConfigIfIndex'
_I='pdnIfAddr'
_H='pdnIfExtIndex'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='PDN-IFEXT-MIB'
_C='deprecated'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
pdnIfExt,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnIfExt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_PdnIfExtConfig_ObjectIdentity=ObjectIdentity
pdnIfExtConfig=_PdnIfExtConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,1))
_PdnIfExtTable_Object=MibTable
pdnIfExtTable=_PdnIfExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1))
if mibBuilder.loadTexts:pdnIfExtTable.setStatus(_A)
_PdnIfExtEntry_Object=MibTableRow
pdnIfExtEntry=_PdnIfExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1,1))
pdnIfExtEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:pdnIfExtEntry.setStatus(_A)
_PdnIfExtIndex_Type=Integer32
_PdnIfExtIndex_Object=MibTableColumn
pdnIfExtIndex=_PdnIfExtIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1,1,1),_PdnIfExtIndex_Type())
pdnIfExtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfExtIndex.setStatus(_A)
_PdnIfExtInOctetRollovers_Type=Counter32
_PdnIfExtInOctetRollovers_Object=MibTableColumn
pdnIfExtInOctetRollovers=_PdnIfExtInOctetRollovers_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1,1,2),_PdnIfExtInOctetRollovers_Type())
pdnIfExtInOctetRollovers.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfExtInOctetRollovers.setStatus(_A)
_PdnIfExtOutOctetRollovers_Type=Counter32
_PdnIfExtOutOctetRollovers_Object=MibTableColumn
pdnIfExtOutOctetRollovers=_PdnIfExtOutOctetRollovers_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1,1,3),_PdnIfExtOutOctetRollovers_Type())
pdnIfExtOutOctetRollovers.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfExtOutOctetRollovers.setStatus(_A)
_PdnIfExtTotalUASs_Type=Counter32
_PdnIfExtTotalUASs_Object=MibTableColumn
pdnIfExtTotalUASs=_PdnIfExtTotalUASs_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,1,1,4),_PdnIfExtTotalUASs_Type())
pdnIfExtTotalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfExtTotalUASs.setStatus(_A)
_PdnIfTable_Object=MibTable
pdnIfTable=_PdnIfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,2))
if mibBuilder.loadTexts:pdnIfTable.setStatus(_C)
_PdnIfEntry_Object=MibTableRow
pdnIfEntry=_PdnIfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,2,1))
pdnIfEntry.setIndexNames((0,_F,_G),(0,_D,_I))
if mibBuilder.loadTexts:pdnIfEntry.setStatus(_C)
_PdnIfAddr_Type=IpAddress
_PdnIfAddr_Object=MibTableColumn
pdnIfAddr=_PdnIfAddr_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,2,1,1),_PdnIfAddr_Type())
pdnIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfAddr.setStatus(_C)
_PdnIfAddrMask_Type=IpAddress
_PdnIfAddrMask_Object=MibTableColumn
pdnIfAddrMask=_PdnIfAddrMask_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,2,1,2),_PdnIfAddrMask_Type())
pdnIfAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnIfAddrMask.setStatus(_C)
_PdnIfStatus_Type=RowStatus
_PdnIfStatus_Object=MibTableColumn
pdnIfStatus=_PdnIfStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,2,1,3),_PdnIfStatus_Type())
pdnIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnIfStatus.setStatus(_C)
_PdnIfExtTestConfig_ObjectIdentity=ObjectIdentity
pdnIfExtTestConfig=_PdnIfExtTestConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,2))
_PdnIfExtTestConfigTable_Object=MibTable
pdnIfExtTestConfigTable=_PdnIfExtTestConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,12,2,1))
if mibBuilder.loadTexts:pdnIfExtTestConfigTable.setStatus(_A)
_PdnIfExtTestConfigEntry_Object=MibTableRow
pdnIfExtTestConfigEntry=_PdnIfExtTestConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,12,2,1,1))
pdnIfExtTestConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:pdnIfExtTestConfigEntry.setStatus(_A)
_PdnIfExtTestConfigIfIndex_Type=Integer32
_PdnIfExtTestConfigIfIndex_Object=MibTableColumn
pdnIfExtTestConfigIfIndex=_PdnIfExtTestConfigIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,12,2,1,1,1),_PdnIfExtTestConfigIfIndex_Type())
pdnIfExtTestConfigIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnIfExtTestConfigIfIndex.setStatus(_A)
_PdnIfExtTestConfigNearTimer_Type=Integer32
_PdnIfExtTestConfigNearTimer_Object=MibTableColumn
pdnIfExtTestConfigNearTimer=_PdnIfExtTestConfigNearTimer_Object((1,3,6,1,4,1,1795,2,24,2,6,12,2,1,1,2),_PdnIfExtTestConfigNearTimer_Type())
pdnIfExtTestConfigNearTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnIfExtTestConfigNearTimer.setStatus(_A)
_PdnIfExtTestConfigFarTimer_Type=Integer32
_PdnIfExtTestConfigFarTimer_Object=MibTableColumn
pdnIfExtTestConfigFarTimer=_PdnIfExtTestConfigFarTimer_Object((1,3,6,1,4,1,1795,2,24,2,6,12,2,1,1,3),_PdnIfExtTestConfigFarTimer_Type())
pdnIfExtTestConfigFarTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnIfExtTestConfigFarTimer.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'pdnIfExtConfig':pdnIfExtConfig,'pdnIfExtTable':pdnIfExtTable,'pdnIfExtEntry':pdnIfExtEntry,_H:pdnIfExtIndex,'pdnIfExtInOctetRollovers':pdnIfExtInOctetRollovers,'pdnIfExtOutOctetRollovers':pdnIfExtOutOctetRollovers,'pdnIfExtTotalUASs':pdnIfExtTotalUASs,'pdnIfTable':pdnIfTable,'pdnIfEntry':pdnIfEntry,_I:pdnIfAddr,'pdnIfAddrMask':pdnIfAddrMask,'pdnIfStatus':pdnIfStatus,'pdnIfExtTestConfig':pdnIfExtTestConfig,'pdnIfExtTestConfigTable':pdnIfExtTestConfigTable,'pdnIfExtTestConfigEntry':pdnIfExtTestConfigEntry,_J:pdnIfExtTestConfigIfIndex,'pdnIfExtTestConfigNearTimer':pdnIfExtTestConfigNearTimer,'pdnIfExtTestConfigFarTimer':pdnIfExtTestConfigFarTimer})