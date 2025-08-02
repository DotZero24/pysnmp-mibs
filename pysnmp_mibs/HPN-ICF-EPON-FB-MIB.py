_F='read-only'
_E='hpnicfEponFBGroupIndex'
_D='HPN-ICF-EPON-FB-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfEponFBMibObjects=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,6))
_HpnicfEponFBMIB_ObjectIdentity=ObjectIdentity
hpnicfEponFBMIB=_HpnicfEponFBMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1))
_HpnicfEponFBMIBTable_Object=MibTable
hpnicfEponFBMIBTable=_HpnicfEponFBMIBTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1))
if mibBuilder.loadTexts:hpnicfEponFBMIBTable.setStatus(_A)
_HpnicfEponFBMIBEntry_Object=MibTableRow
hpnicfEponFBMIBEntry=_HpnicfEponFBMIBEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1))
hpnicfEponFBMIBEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfEponFBMIBEntry.setStatus(_A)
_HpnicfEponFBGroupIndex_Type=Integer32
_HpnicfEponFBGroupIndex_Object=MibTableColumn
hpnicfEponFBGroupIndex=_HpnicfEponFBGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,1),_HpnicfEponFBGroupIndex_Type())
hpnicfEponFBGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfEponFBGroupIndex.setStatus(_A)
_HpnicfEponFBGroupRowStatus_Type=RowStatus
_HpnicfEponFBGroupRowStatus_Object=MibTableColumn
hpnicfEponFBGroupRowStatus=_HpnicfEponFBGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,2),_HpnicfEponFBGroupRowStatus_Type())
hpnicfEponFBGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponFBGroupRowStatus.setStatus(_A)
_HpnicfEponFBMasterPort_Type=Integer32
_HpnicfEponFBMasterPort_Object=MibTableColumn
hpnicfEponFBMasterPort=_HpnicfEponFBMasterPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,3),_HpnicfEponFBMasterPort_Type())
hpnicfEponFBMasterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponFBMasterPort.setStatus(_A)
_HpnicfEponFBSlavePort_Type=Integer32
_HpnicfEponFBSlavePort_Object=MibTableColumn
hpnicfEponFBSlavePort=_HpnicfEponFBSlavePort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,4),_HpnicfEponFBSlavePort_Type())
hpnicfEponFBSlavePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponFBSlavePort.setStatus(_A)
class _HpnicfEponFBMasterPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('down',2)))
_HpnicfEponFBMasterPortStatus_Type.__name__=_B
_HpnicfEponFBMasterPortStatus_Object=MibTableColumn
hpnicfEponFBMasterPortStatus=_HpnicfEponFBMasterPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,5),_HpnicfEponFBMasterPortStatus_Type())
hpnicfEponFBMasterPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfEponFBMasterPortStatus.setStatus(_A)
class _HpnicfEponFBSlavePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),('down',2)))
_HpnicfEponFBSlavePortStatus_Type.__name__=_B
_HpnicfEponFBSlavePortStatus_Object=MibTableColumn
hpnicfEponFBSlavePortStatus=_HpnicfEponFBSlavePortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,6),_HpnicfEponFBSlavePortStatus_Type())
hpnicfEponFBSlavePortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfEponFBSlavePortStatus.setStatus(_A)
class _HpnicfEponFBSwitchover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_HpnicfEponFBSwitchover_Type.__name__=_B
_HpnicfEponFBSwitchover_Object=MibTableColumn
hpnicfEponFBSwitchover=_HpnicfEponFBSwitchover_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,6,1,1,1,7),_HpnicfEponFBSwitchover_Type())
hpnicfEponFBSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfEponFBSwitchover.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfEponFBMibObjects':hpnicfEponFBMibObjects,'hpnicfEponFBMIB':hpnicfEponFBMIB,'hpnicfEponFBMIBTable':hpnicfEponFBMIBTable,'hpnicfEponFBMIBEntry':hpnicfEponFBMIBEntry,_E:hpnicfEponFBGroupIndex,'hpnicfEponFBGroupRowStatus':hpnicfEponFBGroupRowStatus,'hpnicfEponFBMasterPort':hpnicfEponFBMasterPort,'hpnicfEponFBSlavePort':hpnicfEponFBSlavePort,'hpnicfEponFBMasterPortStatus':hpnicfEponFBMasterPortStatus,'hpnicfEponFBSlavePortStatus':hpnicfEponFBSlavePortStatus,'hpnicfEponFBSwitchover':hpnicfEponFBSwitchover})