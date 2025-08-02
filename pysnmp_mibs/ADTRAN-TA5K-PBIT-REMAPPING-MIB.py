_J='read-only'
_I='read-create'
_H='not-accessible'
_G='adTa5kPbitRemappingIngressPriority'
_F='adTa5kPbitRemappingIngressVlanID'
_E='ifIndex'
_D='IF-MIB'
_C='ADTRAN-TA5K-PBIT-REMAPPING-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTa5kPbitRemapping,adTa5kPbitRemappingID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adTa5kPbitRemapping','adTa5kPbitRemappingID')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adTa5kPbitRemappingModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,38,1))
if mibBuilder.loadTexts:adTa5kPbitRemappingModuleIdentity.setRevisions(('2013-02-18 20:30',))
_AdTa5kPbitRemappingProvisioning_ObjectIdentity=ObjectIdentity
adTa5kPbitRemappingProvisioning=_AdTa5kPbitRemappingProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,38,1))
_AdTa5kPbitRemappingTable_Object=MibTable
adTa5kPbitRemappingTable=_AdTa5kPbitRemappingTable_Object((1,3,6,1,4,1,664,5,67,1,38,1,1))
if mibBuilder.loadTexts:adTa5kPbitRemappingTable.setStatus(_A)
_AdTa5kPbitRemappingEntry_Object=MibTableRow
adTa5kPbitRemappingEntry=_AdTa5kPbitRemappingEntry_Object((1,3,6,1,4,1,664,5,67,1,38,1,1,1))
adTa5kPbitRemappingEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:adTa5kPbitRemappingEntry.setStatus(_A)
class _AdTa5kPbitRemappingIngressVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AdTa5kPbitRemappingIngressVlanID_Type.__name__=_B
_AdTa5kPbitRemappingIngressVlanID_Object=MibTableColumn
adTa5kPbitRemappingIngressVlanID=_AdTa5kPbitRemappingIngressVlanID_Object((1,3,6,1,4,1,664,5,67,1,38,1,1,1,1),_AdTa5kPbitRemappingIngressVlanID_Type())
adTa5kPbitRemappingIngressVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kPbitRemappingIngressVlanID.setStatus(_A)
class _AdTa5kPbitRemappingIngressPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdTa5kPbitRemappingIngressPriority_Type.__name__=_B
_AdTa5kPbitRemappingIngressPriority_Object=MibTableColumn
adTa5kPbitRemappingIngressPriority=_AdTa5kPbitRemappingIngressPriority_Object((1,3,6,1,4,1,664,5,67,1,38,1,1,1,2),_AdTa5kPbitRemappingIngressPriority_Type())
adTa5kPbitRemappingIngressPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kPbitRemappingIngressPriority.setStatus(_A)
class _AdTa5kPbitRemappingNewPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdTa5kPbitRemappingNewPriority_Type.__name__=_B
_AdTa5kPbitRemappingNewPriority_Object=MibTableColumn
adTa5kPbitRemappingNewPriority=_AdTa5kPbitRemappingNewPriority_Object((1,3,6,1,4,1,664,5,67,1,38,1,1,1,3),_AdTa5kPbitRemappingNewPriority_Type())
adTa5kPbitRemappingNewPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:adTa5kPbitRemappingNewPriority.setStatus(_A)
_AdTa5kPbitRemappingRowStatus_Type=RowStatus
_AdTa5kPbitRemappingRowStatus_Object=MibTableColumn
adTa5kPbitRemappingRowStatus=_AdTa5kPbitRemappingRowStatus_Object((1,3,6,1,4,1,664,5,67,1,38,1,1,1,4),_AdTa5kPbitRemappingRowStatus_Type())
adTa5kPbitRemappingRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:adTa5kPbitRemappingRowStatus.setStatus(_A)
_AdTa5kPbitRemappingStatus_ObjectIdentity=ObjectIdentity
adTa5kPbitRemappingStatus=_AdTa5kPbitRemappingStatus_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,38,2))
_AdTa5kPbitRemappingMaxSupported_Type=Integer32
_AdTa5kPbitRemappingMaxSupported_Object=MibScalar
adTa5kPbitRemappingMaxSupported=_AdTa5kPbitRemappingMaxSupported_Object((1,3,6,1,4,1,664,5,67,1,38,2,1),_AdTa5kPbitRemappingMaxSupported_Type())
adTa5kPbitRemappingMaxSupported.setMaxAccess(_J)
if mibBuilder.loadTexts:adTa5kPbitRemappingMaxSupported.setStatus(_A)
_AdTa5kPbitRemappingLastError_Type=DisplayString
_AdTa5kPbitRemappingLastError_Object=MibScalar
adTa5kPbitRemappingLastError=_AdTa5kPbitRemappingLastError_Object((1,3,6,1,4,1,664,5,67,1,38,2,2),_AdTa5kPbitRemappingLastError_Type())
adTa5kPbitRemappingLastError.setMaxAccess(_J)
if mibBuilder.loadTexts:adTa5kPbitRemappingLastError.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adTa5kPbitRemappingProvisioning':adTa5kPbitRemappingProvisioning,'adTa5kPbitRemappingTable':adTa5kPbitRemappingTable,'adTa5kPbitRemappingEntry':adTa5kPbitRemappingEntry,_F:adTa5kPbitRemappingIngressVlanID,_G:adTa5kPbitRemappingIngressPriority,'adTa5kPbitRemappingNewPriority':adTa5kPbitRemappingNewPriority,'adTa5kPbitRemappingRowStatus':adTa5kPbitRemappingRowStatus,'adTa5kPbitRemappingStatus':adTa5kPbitRemappingStatus,'adTa5kPbitRemappingMaxSupported':adTa5kPbitRemappingMaxSupported,'adTa5kPbitRemappingLastError':adTa5kPbitRemappingLastError,'adTa5kPbitRemappingModuleIdentity':adTa5kPbitRemappingModuleIdentity})