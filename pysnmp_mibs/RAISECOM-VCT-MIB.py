_K='ifIndex'
_J='IF-MIB'
_I='OctetString'
_H='invalidation'
_G='error'
_F='shorted'
_E='open'
_D='normal'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
raisecomVct=ModuleIdentity((1,3,6,1,4,1,8886,1,14))
if mibBuilder.loadTexts:raisecomVct.setRevisions(('2006-09-08 00:00',))
_RaisecomVctPortObjects_ObjectIdentity=ObjectIdentity
raisecomVctPortObjects=_RaisecomVctPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,14,1))
_RaisecomVctPortTable_Object=MibTable
raisecomVctPortTable=_RaisecomVctPortTable_Object((1,3,6,1,4,1,8886,1,14,1,1))
if mibBuilder.loadTexts:raisecomVctPortTable.setStatus(_A)
_RaisecomVctPortEntry_Object=MibTableRow
raisecomVctPortEntry=_RaisecomVctPortEntry_Object((1,3,6,1,4,1,8886,1,14,1,1,1))
raisecomVctPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:raisecomVctPortEntry.setStatus(_A)
class _RaisecomVctPortAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unSupported',1),('neverIssued',2),('issued',3),('testing',4)))
_RaisecomVctPortAttribute_Type.__name__=_C
_RaisecomVctPortAttribute_Object=MibTableColumn
raisecomVctPortAttribute=_RaisecomVctPortAttribute_Object((1,3,6,1,4,1,8886,1,14,1,1,1,1),_RaisecomVctPortAttribute_Type())
raisecomVctPortAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortAttribute.setStatus(_A)
class _RaisecomVctPortIssuedTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomVctPortIssuedTime_Type.__name__=_I
_RaisecomVctPortIssuedTime_Object=MibTableColumn
raisecomVctPortIssuedTime=_RaisecomVctPortIssuedTime_Object((1,3,6,1,4,1,8886,1,14,1,1,1,2),_RaisecomVctPortIssuedTime_Type())
raisecomVctPortIssuedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortIssuedTime.setStatus(_A)
class _RaisecomVctPortCableTXStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5)))
_RaisecomVctPortCableTXStatus_Type.__name__=_C
_RaisecomVctPortCableTXStatus_Object=MibTableColumn
raisecomVctPortCableTXStatus=_RaisecomVctPortCableTXStatus_Object((1,3,6,1,4,1,8886,1,14,1,1,1,3),_RaisecomVctPortCableTXStatus_Type())
raisecomVctPortCableTXStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableTXStatus.setStatus(_A)
_RaisecomVctPortCableTXLength_Type=Integer32
_RaisecomVctPortCableTXLength_Object=MibTableColumn
raisecomVctPortCableTXLength=_RaisecomVctPortCableTXLength_Object((1,3,6,1,4,1,8886,1,14,1,1,1,4),_RaisecomVctPortCableTXLength_Type())
raisecomVctPortCableTXLength.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableTXLength.setStatus(_A)
class _RaisecomVctPortCableRXStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5)))
_RaisecomVctPortCableRXStatus_Type.__name__=_C
_RaisecomVctPortCableRXStatus_Object=MibTableColumn
raisecomVctPortCableRXStatus=_RaisecomVctPortCableRXStatus_Object((1,3,6,1,4,1,8886,1,14,1,1,1,5),_RaisecomVctPortCableRXStatus_Type())
raisecomVctPortCableRXStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableRXStatus.setStatus(_A)
_RaisecomVctPortCableRXLength_Type=Integer32
_RaisecomVctPortCableRXLength_Object=MibTableColumn
raisecomVctPortCableRXLength=_RaisecomVctPortCableRXLength_Object((1,3,6,1,4,1,8886,1,14,1,1,1,6),_RaisecomVctPortCableRXLength_Type())
raisecomVctPortCableRXLength.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableRXLength.setStatus(_A)
class _RaisecomVctPortCableTX2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5)))
_RaisecomVctPortCableTX2Status_Type.__name__=_C
_RaisecomVctPortCableTX2Status_Object=MibTableColumn
raisecomVctPortCableTX2Status=_RaisecomVctPortCableTX2Status_Object((1,3,6,1,4,1,8886,1,14,1,1,1,7),_RaisecomVctPortCableTX2Status_Type())
raisecomVctPortCableTX2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableTX2Status.setStatus(_A)
_RaisecomVctPortCableTX2Length_Type=Integer32
_RaisecomVctPortCableTX2Length_Object=MibTableColumn
raisecomVctPortCableTX2Length=_RaisecomVctPortCableTX2Length_Object((1,3,6,1,4,1,8886,1,14,1,1,1,8),_RaisecomVctPortCableTX2Length_Type())
raisecomVctPortCableTX2Length.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableTX2Length.setStatus(_A)
class _RaisecomVctPortCableRX2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5)))
_RaisecomVctPortCableRX2Status_Type.__name__=_C
_RaisecomVctPortCableRX2Status_Object=MibTableColumn
raisecomVctPortCableRX2Status=_RaisecomVctPortCableRX2Status_Object((1,3,6,1,4,1,8886,1,14,1,1,1,9),_RaisecomVctPortCableRX2Status_Type())
raisecomVctPortCableRX2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableRX2Status.setStatus(_A)
_RaisecomVctPortCableRX2Length_Type=Integer32
_RaisecomVctPortCableRX2Length_Object=MibTableColumn
raisecomVctPortCableRX2Length=_RaisecomVctPortCableRX2Length_Object((1,3,6,1,4,1,8886,1,14,1,1,1,10),_RaisecomVctPortCableRX2Length_Type())
raisecomVctPortCableRX2Length.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableRX2Length.setStatus(_A)
_RaisecomVctPortCableLengthFuzz_Type=Integer32
_RaisecomVctPortCableLengthFuzz_Object=MibTableColumn
raisecomVctPortCableLengthFuzz=_RaisecomVctPortCableLengthFuzz_Object((1,3,6,1,4,1,8886,1,14,1,1,1,11),_RaisecomVctPortCableLengthFuzz_Type())
raisecomVctPortCableLengthFuzz.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVctPortCableLengthFuzz.setStatus(_A)
_RaisecomVctPortStartTest_Type=Integer32
_RaisecomVctPortStartTest_Object=MibScalar
raisecomVctPortStartTest=_RaisecomVctPortStartTest_Object((1,3,6,1,4,1,8886,1,14,1,2),_RaisecomVctPortStartTest_Type())
raisecomVctPortStartTest.setMaxAccess('read-write')
if mibBuilder.loadTexts:raisecomVctPortStartTest.setStatus(_A)
mibBuilder.exportSymbols('RAISECOM-VCT-MIB',**{'raisecomVct':raisecomVct,'raisecomVctPortObjects':raisecomVctPortObjects,'raisecomVctPortTable':raisecomVctPortTable,'raisecomVctPortEntry':raisecomVctPortEntry,'raisecomVctPortAttribute':raisecomVctPortAttribute,'raisecomVctPortIssuedTime':raisecomVctPortIssuedTime,'raisecomVctPortCableTXStatus':raisecomVctPortCableTXStatus,'raisecomVctPortCableTXLength':raisecomVctPortCableTXLength,'raisecomVctPortCableRXStatus':raisecomVctPortCableRXStatus,'raisecomVctPortCableRXLength':raisecomVctPortCableRXLength,'raisecomVctPortCableTX2Status':raisecomVctPortCableTX2Status,'raisecomVctPortCableTX2Length':raisecomVctPortCableTX2Length,'raisecomVctPortCableRX2Status':raisecomVctPortCableRX2Status,'raisecomVctPortCableRX2Length':raisecomVctPortCableRX2Length,'raisecomVctPortCableLengthFuzz':raisecomVctPortCableLengthFuzz,'raisecomVctPortStartTest':raisecomVctPortStartTest})