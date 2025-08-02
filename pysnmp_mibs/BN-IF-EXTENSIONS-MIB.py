_R='advertise2500Full'
_Q='advertise40000Full'
_P='advertise10000Full'
_O='advertiseAsymmPauseFrame'
_N='advertisePauseFrame'
_M='advertise1000Full'
_L='advertise1000Half'
_K='advertise100Full'
_J='advertise100Half'
_I='advertise10Full'
_H='advertise10Half'
_G='bnIfExtnIndex'
_F='BN-IF-EXTENSIONS-MIB'
_E='read-write'
_D='Bits'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5IfExt,=mibBuilder.importSymbols('S5-ROOT-MIB','s5IfExt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bnIfExtensionsMib=ModuleIdentity((1,3,6,1,4,1,45,1,6,15,2))
if mibBuilder.loadTexts:bnIfExtensionsMib.setRevisions(('2016-11-28 00:00','2013-07-26 00:00','2011-10-05 00:00','2011-09-16 00:00','2004-07-20 00:00'))
_BnIfExtensions_ObjectIdentity=ObjectIdentity
bnIfExtensions=_BnIfExtensions_ObjectIdentity((1,3,6,1,4,1,45,1,6,15,1))
_BnIfExtnTable_Object=MibTable
bnIfExtnTable=_BnIfExtnTable_Object((1,3,6,1,4,1,45,1,6,15,1,1))
if mibBuilder.loadTexts:bnIfExtnTable.setStatus(_A)
_BnIfExtnEntry_Object=MibTableRow
bnIfExtnEntry=_BnIfExtnEntry_Object((1,3,6,1,4,1,45,1,6,15,1,1,1))
bnIfExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:bnIfExtnEntry.setStatus(_A)
_BnIfExtnIndex_Type=Integer32
_BnIfExtnIndex_Object=MibTableColumn
bnIfExtnIndex=_BnIfExtnIndex_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,1),_BnIfExtnIndex_Type())
bnIfExtnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bnIfExtnIndex.setStatus(_A)
_BnIfExtnSlot_Type=Integer32
_BnIfExtnSlot_Object=MibTableColumn
bnIfExtnSlot=_BnIfExtnSlot_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,2),_BnIfExtnSlot_Type())
bnIfExtnSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:bnIfExtnSlot.setStatus(_A)
_BnIfExtnPort_Type=Integer32
_BnIfExtnPort_Object=MibTableColumn
bnIfExtnPort=_BnIfExtnPort_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,3),_BnIfExtnPort_Type())
bnIfExtnPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bnIfExtnPort.setStatus(_A)
class _BnIfExtnIsPortShared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portShared',1),('portNotShared',2)))
_BnIfExtnIsPortShared_Type.__name__=_C
_BnIfExtnIsPortShared_Object=MibTableColumn
bnIfExtnIsPortShared=_BnIfExtnIsPortShared_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,4),_BnIfExtnIsPortShared_Type())
bnIfExtnIsPortShared.setMaxAccess(_B)
if mibBuilder.loadTexts:bnIfExtnIsPortShared.setStatus(_A)
class _BnIfExtnPortActiveComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fixedPort',1),('gbicPort',2),('mdaPort',3)))
_BnIfExtnPortActiveComponent_Type.__name__=_C
_BnIfExtnPortActiveComponent_Object=MibTableColumn
bnIfExtnPortActiveComponent=_BnIfExtnPortActiveComponent_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,5),_BnIfExtnPortActiveComponent_Type())
bnIfExtnPortActiveComponent.setMaxAccess(_E)
if mibBuilder.loadTexts:bnIfExtnPortActiveComponent.setStatus(_A)
class _BnIfExtnPoweredDeviceDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('compliantWith802dot3af',1),('compliantWith802dot3afAndLegacySupport',2),('compliantWith802dot3at',3),('compliantWith802dot3atAndLegacySupport',4)))
_BnIfExtnPoweredDeviceDetectType_Type.__name__=_C
_BnIfExtnPoweredDeviceDetectType_Object=MibTableColumn
bnIfExtnPoweredDeviceDetectType=_BnIfExtnPoweredDeviceDetectType_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,6),_BnIfExtnPoweredDeviceDetectType_Type())
bnIfExtnPoweredDeviceDetectType.setMaxAccess(_E)
if mibBuilder.loadTexts:bnIfExtnPoweredDeviceDetectType.setStatus(_A)
class _BnIfExtnAutoNegotiationExtAdv_Type(Bits):namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8),(_Q,9),(_R,10)))
_BnIfExtnAutoNegotiationExtAdv_Type.__name__=_D
_BnIfExtnAutoNegotiationExtAdv_Object=MibTableColumn
bnIfExtnAutoNegotiationExtAdv=_BnIfExtnAutoNegotiationExtAdv_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,7),_BnIfExtnAutoNegotiationExtAdv_Type())
bnIfExtnAutoNegotiationExtAdv.setMaxAccess(_E)
if mibBuilder.loadTexts:bnIfExtnAutoNegotiationExtAdv.setStatus(_A)
class _BnIfExtnExtHwAdvCapability_Type(Bits):namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8),(_Q,9),(_R,10)))
_BnIfExtnExtHwAdvCapability_Type.__name__=_D
_BnIfExtnExtHwAdvCapability_Object=MibTableColumn
bnIfExtnExtHwAdvCapability=_BnIfExtnExtHwAdvCapability_Object((1,3,6,1,4,1,45,1,6,15,1,1,1,8),_BnIfExtnExtHwAdvCapability_Type())
bnIfExtnExtHwAdvCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:bnIfExtnExtHwAdvCapability.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'bnIfExtensions':bnIfExtensions,'bnIfExtnTable':bnIfExtnTable,'bnIfExtnEntry':bnIfExtnEntry,_G:bnIfExtnIndex,'bnIfExtnSlot':bnIfExtnSlot,'bnIfExtnPort':bnIfExtnPort,'bnIfExtnIsPortShared':bnIfExtnIsPortShared,'bnIfExtnPortActiveComponent':bnIfExtnPortActiveComponent,'bnIfExtnPoweredDeviceDetectType':bnIfExtnPoweredDeviceDetectType,'bnIfExtnAutoNegotiationExtAdv':bnIfExtnAutoNegotiationExtAdv,'bnIfExtnExtHwAdvCapability':bnIfExtnExtHwAdvCapability,'bnIfExtensionsMib':bnIfExtensionsMib})