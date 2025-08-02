_J='DisplayString'
_I='IpAddress'
_H='Counter32'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='clear'
_C='noaction'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_H,'Counter64','Gauge32',_B,_I,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
Counter32,IpAddress=mibBuilder.importSymbols('SNMPv2-SMI-v1',_H,_I)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
DisplayString,=mibBuilder.importSymbols('SNMPv2-TC-v1',_J)
_IbmIROCroutinginterface_ObjectIdentity=ObjectIdentity
ibmIROCroutinginterface=_IbmIROCroutinginterface_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,17))
_IbminterfaceClearTable_Object=MibTable
ibminterfaceClearTable=_IbminterfaceClearTable_Object((1,3,6,1,4,1,2,6,119,4,17,1))
if mibBuilder.loadTexts:ibminterfaceClearTable.setStatus(_A)
_IbminterfaceClearEntry_Object=MibTableRow
ibminterfaceClearEntry=_IbminterfaceClearEntry_Object((1,3,6,1,4,1,2,6,119,4,17,1,1))
ibminterfaceClearEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ibminterfaceClearEntry.setStatus(_A)
class _IbminterfaceClearInOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearInOctets_Type.__name__=_B
_IbminterfaceClearInOctets_Object=MibTableColumn
ibminterfaceClearInOctets=_IbminterfaceClearInOctets_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,1),_IbminterfaceClearInOctets_Type())
ibminterfaceClearInOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearInOctets.setStatus(_A)
class _IbminterfaceClearInUcastPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearInUcastPkts_Type.__name__=_B
_IbminterfaceClearInUcastPkts_Object=MibTableColumn
ibminterfaceClearInUcastPkts=_IbminterfaceClearInUcastPkts_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,2),_IbminterfaceClearInUcastPkts_Type())
ibminterfaceClearInUcastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearInUcastPkts.setStatus(_A)
class _IbminterfaceClearInMulticastPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearInMulticastPkts_Type.__name__=_B
_IbminterfaceClearInMulticastPkts_Object=MibTableColumn
ibminterfaceClearInMulticastPkts=_IbminterfaceClearInMulticastPkts_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,3),_IbminterfaceClearInMulticastPkts_Type())
ibminterfaceClearInMulticastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearInMulticastPkts.setStatus(_A)
class _IbminterfaceClearInErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearInErrors_Type.__name__=_B
_IbminterfaceClearInErrors_Object=MibTableColumn
ibminterfaceClearInErrors=_IbminterfaceClearInErrors_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,4),_IbminterfaceClearInErrors_Type())
ibminterfaceClearInErrors.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearInErrors.setStatus(_A)
class _IbminterfaceClearInAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearInAll_Type.__name__=_B
_IbminterfaceClearInAll_Object=MibTableColumn
ibminterfaceClearInAll=_IbminterfaceClearInAll_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,5),_IbminterfaceClearInAll_Type())
ibminterfaceClearInAll.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearInAll.setStatus(_A)
class _IbminterfaceClearOutOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearOutOctets_Type.__name__=_B
_IbminterfaceClearOutOctets_Object=MibTableColumn
ibminterfaceClearOutOctets=_IbminterfaceClearOutOctets_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,6),_IbminterfaceClearOutOctets_Type())
ibminterfaceClearOutOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearOutOctets.setStatus(_A)
class _IbminterfaceClearOutUcastPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearOutUcastPkts_Type.__name__=_B
_IbminterfaceClearOutUcastPkts_Object=MibTableColumn
ibminterfaceClearOutUcastPkts=_IbminterfaceClearOutUcastPkts_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,7),_IbminterfaceClearOutUcastPkts_Type())
ibminterfaceClearOutUcastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearOutUcastPkts.setStatus(_A)
class _IbminterfaceClearOutMulticastPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearOutMulticastPkts_Type.__name__=_B
_IbminterfaceClearOutMulticastPkts_Object=MibTableColumn
ibminterfaceClearOutMulticastPkts=_IbminterfaceClearOutMulticastPkts_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,8),_IbminterfaceClearOutMulticastPkts_Type())
ibminterfaceClearOutMulticastPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearOutMulticastPkts.setStatus(_A)
class _IbminterfaceClearOutErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearOutErrors_Type.__name__=_B
_IbminterfaceClearOutErrors_Object=MibTableColumn
ibminterfaceClearOutErrors=_IbminterfaceClearOutErrors_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,9),_IbminterfaceClearOutErrors_Type())
ibminterfaceClearOutErrors.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearOutErrors.setStatus(_A)
class _IbminterfaceClearOutAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearOutAll_Type.__name__=_B
_IbminterfaceClearOutAll_Object=MibTableColumn
ibminterfaceClearOutAll=_IbminterfaceClearOutAll_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,10),_IbminterfaceClearOutAll_Type())
ibminterfaceClearOutAll.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearOutAll.setStatus(_A)
class _IbminterfaceClearMaintTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearMaintTest_Type.__name__=_B
_IbminterfaceClearMaintTest_Object=MibTableColumn
ibminterfaceClearMaintTest=_IbminterfaceClearMaintTest_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,11),_IbminterfaceClearMaintTest_Type())
ibminterfaceClearMaintTest.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearMaintTest.setStatus(_A)
class _IbminterfaceClearDeviceSpecific_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearDeviceSpecific_Type.__name__=_B
_IbminterfaceClearDeviceSpecific_Object=MibTableColumn
ibminterfaceClearDeviceSpecific=_IbminterfaceClearDeviceSpecific_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,12),_IbminterfaceClearDeviceSpecific_Type())
ibminterfaceClearDeviceSpecific.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearDeviceSpecific.setStatus(_A)
class _IbminterfaceClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_IbminterfaceClearAll_Type.__name__=_B
_IbminterfaceClearAll_Object=MibTableColumn
ibminterfaceClearAll=_IbminterfaceClearAll_Object((1,3,6,1,4,1,2,6,119,4,17,1,1,13),_IbminterfaceClearAll_Type())
ibminterfaceClearAll.setMaxAccess(_E)
if mibBuilder.loadTexts:ibminterfaceClearAll.setStatus(_A)
mibBuilder.exportSymbols('IBM-INTERFACE-MIB',**{'ibmIROCroutinginterface':ibmIROCroutinginterface,'ibminterfaceClearTable':ibminterfaceClearTable,'ibminterfaceClearEntry':ibminterfaceClearEntry,'ibminterfaceClearInOctets':ibminterfaceClearInOctets,'ibminterfaceClearInUcastPkts':ibminterfaceClearInUcastPkts,'ibminterfaceClearInMulticastPkts':ibminterfaceClearInMulticastPkts,'ibminterfaceClearInErrors':ibminterfaceClearInErrors,'ibminterfaceClearInAll':ibminterfaceClearInAll,'ibminterfaceClearOutOctets':ibminterfaceClearOutOctets,'ibminterfaceClearOutUcastPkts':ibminterfaceClearOutUcastPkts,'ibminterfaceClearOutMulticastPkts':ibminterfaceClearOutMulticastPkts,'ibminterfaceClearOutErrors':ibminterfaceClearOutErrors,'ibminterfaceClearOutAll':ibminterfaceClearOutAll,'ibminterfaceClearMaintTest':ibminterfaceClearMaintTest,'ibminterfaceClearDeviceSpecific':ibminterfaceClearDeviceSpecific,'ibminterfaceClearAll':ibminterfaceClearAll})