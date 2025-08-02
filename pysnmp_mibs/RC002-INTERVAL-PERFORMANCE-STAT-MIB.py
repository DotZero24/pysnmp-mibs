_K='rcftSlotLANFxIntervalNumber'
_J='rcftSlotWANFxIntervalNumber'
_I='rcftSlotLANFxPortIndex'
_H='rcftSlotWANFxPortIndex'
_G='rcftSlotIndex'
_F='rcftChassisIndex'
_E='RC002-INTERVAL-PERFORMANCE-STAT-MIB'
_D='RAISECOM-RCFT-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rcftChassisIndex,rcftMibObjects,rcftSlotIndex,rcftSlotStat=mibBuilder.importSymbols(_D,_F,'rcftMibObjects',_G,'rcftSlotStat')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
_RcftSlotWANFxPortCurrentTable_Object=MibTable
rcftSlotWANFxPortCurrentTable=_RcftSlotWANFxPortCurrentTable_Object((1,3,6,1,4,1,8886,2,1,5,4))
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentTable.setStatus(_A)
_RcftSlotWANFxPortCurrentEntry_Object=MibTableRow
rcftSlotWANFxPortCurrentEntry=_RcftSlotWANFxPortCurrentEntry_Object((1,3,6,1,4,1,8886,2,1,5,4,1))
rcftSlotWANFxPortCurrentEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_H))
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentEntry.setStatus(_A)
_RcftSlotWANFxPortIndex_Type=Integer32
_RcftSlotWANFxPortIndex_Object=MibTableColumn
rcftSlotWANFxPortIndex=_RcftSlotWANFxPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,4,1,1),_RcftSlotWANFxPortIndex_Type())
rcftSlotWANFxPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIndex.setStatus(_A)
class _RcftSlotWANFxPortCurrentTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortCurrentTemperature_Type.__name__=_C
_RcftSlotWANFxPortCurrentTemperature_Object=MibTableColumn
rcftSlotWANFxPortCurrentTemperature=_RcftSlotWANFxPortCurrentTemperature_Object((1,3,6,1,4,1,8886,2,1,5,4,1,2),_RcftSlotWANFxPortCurrentTemperature_Type())
rcftSlotWANFxPortCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentTemperature.setStatus(_A)
class _RcftSlotWANFxPortCurrentVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortCurrentVoltage_Type.__name__=_C
_RcftSlotWANFxPortCurrentVoltage_Object=MibTableColumn
rcftSlotWANFxPortCurrentVoltage=_RcftSlotWANFxPortCurrentVoltage_Object((1,3,6,1,4,1,8886,2,1,5,4,1,3),_RcftSlotWANFxPortCurrentVoltage_Type())
rcftSlotWANFxPortCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentVoltage.setStatus(_A)
class _RcftSlotWANFxPortCurrentOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortCurrentOffsetCurr_Type.__name__=_C
_RcftSlotWANFxPortCurrentOffsetCurr_Object=MibTableColumn
rcftSlotWANFxPortCurrentOffsetCurr=_RcftSlotWANFxPortCurrentOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,4,1,4),_RcftSlotWANFxPortCurrentOffsetCurr_Type())
rcftSlotWANFxPortCurrentOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentOffsetCurr.setStatus(_A)
class _RcftSlotWANFxPortCurrentRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortCurrentRecvPower_Type.__name__=_C
_RcftSlotWANFxPortCurrentRecvPower_Object=MibTableColumn
rcftSlotWANFxPortCurrentRecvPower=_RcftSlotWANFxPortCurrentRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,4,1,5),_RcftSlotWANFxPortCurrentRecvPower_Type())
rcftSlotWANFxPortCurrentRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentRecvPower.setStatus(_A)
class _RcftSlotWANFxPortCurrentSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortCurrentSendPower_Type.__name__=_C
_RcftSlotWANFxPortCurrentSendPower_Object=MibTableColumn
rcftSlotWANFxPortCurrentSendPower=_RcftSlotWANFxPortCurrentSendPower_Object((1,3,6,1,4,1,8886,2,1,5,4,1,6),_RcftSlotWANFxPortCurrentSendPower_Type())
rcftSlotWANFxPortCurrentSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortCurrentSendPower.setStatus(_A)
_RcftSlotWANFxPortIntervalTable_Object=MibTable
rcftSlotWANFxPortIntervalTable=_RcftSlotWANFxPortIntervalTable_Object((1,3,6,1,4,1,8886,2,1,5,5))
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalTable.setStatus(_A)
_RcftSlotWANFxPortIntervalEntry_Object=MibTableRow
rcftSlotWANFxPortIntervalEntry=_RcftSlotWANFxPortIntervalEntry_Object((1,3,6,1,4,1,8886,2,1,5,5,1))
rcftSlotWANFxPortIntervalEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalEntry.setStatus(_A)
_RcftSlotWANFxIntervalNumber_Type=Integer32
_RcftSlotWANFxIntervalNumber_Object=MibTableColumn
rcftSlotWANFxIntervalNumber=_RcftSlotWANFxIntervalNumber_Object((1,3,6,1,4,1,8886,2,1,5,5,1,1),_RcftSlotWANFxIntervalNumber_Type())
rcftSlotWANFxIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxIntervalNumber.setStatus(_A)
class _RcftSlotWANFxPortIntervalTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortIntervalTemperature_Type.__name__=_C
_RcftSlotWANFxPortIntervalTemperature_Object=MibTableColumn
rcftSlotWANFxPortIntervalTemperature=_RcftSlotWANFxPortIntervalTemperature_Object((1,3,6,1,4,1,8886,2,1,5,5,1,2),_RcftSlotWANFxPortIntervalTemperature_Type())
rcftSlotWANFxPortIntervalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalTemperature.setStatus(_A)
class _RcftSlotWANFxPortIntervalVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortIntervalVoltage_Type.__name__=_C
_RcftSlotWANFxPortIntervalVoltage_Object=MibTableColumn
rcftSlotWANFxPortIntervalVoltage=_RcftSlotWANFxPortIntervalVoltage_Object((1,3,6,1,4,1,8886,2,1,5,5,1,3),_RcftSlotWANFxPortIntervalVoltage_Type())
rcftSlotWANFxPortIntervalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalVoltage.setStatus(_A)
class _RcftSlotWANFxPortIntervalOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortIntervalOffsetCurr_Type.__name__=_C
_RcftSlotWANFxPortIntervalOffsetCurr_Object=MibTableColumn
rcftSlotWANFxPortIntervalOffsetCurr=_RcftSlotWANFxPortIntervalOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,5,1,4),_RcftSlotWANFxPortIntervalOffsetCurr_Type())
rcftSlotWANFxPortIntervalOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalOffsetCurr.setStatus(_A)
class _RcftSlotWANFxPortIntervalRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortIntervalRecvPower_Type.__name__=_C
_RcftSlotWANFxPortIntervalRecvPower_Object=MibTableColumn
rcftSlotWANFxPortIntervalRecvPower=_RcftSlotWANFxPortIntervalRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,5,1,5),_RcftSlotWANFxPortIntervalRecvPower_Type())
rcftSlotWANFxPortIntervalRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalRecvPower.setStatus(_A)
class _RcftSlotWANFxPortIntervalSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortIntervalSendPower_Type.__name__=_C
_RcftSlotWANFxPortIntervalSendPower_Object=MibTableColumn
rcftSlotWANFxPortIntervalSendPower=_RcftSlotWANFxPortIntervalSendPower_Object((1,3,6,1,4,1,8886,2,1,5,5,1,6),_RcftSlotWANFxPortIntervalSendPower_Type())
rcftSlotWANFxPortIntervalSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortIntervalSendPower.setStatus(_A)
_RcftSlotLANFxPortCurrentTable_Object=MibTable
rcftSlotLANFxPortCurrentTable=_RcftSlotLANFxPortCurrentTable_Object((1,3,6,1,4,1,8886,2,1,5,6))
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentTable.setStatus(_A)
_RcftSlotLANFxPortCurrentEntry_Object=MibTableRow
rcftSlotLANFxPortCurrentEntry=_RcftSlotLANFxPortCurrentEntry_Object((1,3,6,1,4,1,8886,2,1,5,6,1))
rcftSlotLANFxPortCurrentEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_I))
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentEntry.setStatus(_A)
_RcftSlotLANFxPortIndex_Type=Integer32
_RcftSlotLANFxPortIndex_Object=MibTableColumn
rcftSlotLANFxPortIndex=_RcftSlotLANFxPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,6,1,1),_RcftSlotLANFxPortIndex_Type())
rcftSlotLANFxPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIndex.setStatus(_A)
class _RcftSlotLANFxPortCurrentTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortCurrentTemperature_Type.__name__=_C
_RcftSlotLANFxPortCurrentTemperature_Object=MibTableColumn
rcftSlotLANFxPortCurrentTemperature=_RcftSlotLANFxPortCurrentTemperature_Object((1,3,6,1,4,1,8886,2,1,5,6,1,2),_RcftSlotLANFxPortCurrentTemperature_Type())
rcftSlotLANFxPortCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentTemperature.setStatus(_A)
class _RcftSlotLANFxPortCurrentVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortCurrentVoltage_Type.__name__=_C
_RcftSlotLANFxPortCurrentVoltage_Object=MibTableColumn
rcftSlotLANFxPortCurrentVoltage=_RcftSlotLANFxPortCurrentVoltage_Object((1,3,6,1,4,1,8886,2,1,5,6,1,3),_RcftSlotLANFxPortCurrentVoltage_Type())
rcftSlotLANFxPortCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentVoltage.setStatus(_A)
class _RcftSlotLANFxPortCurrentOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortCurrentOffsetCurr_Type.__name__=_C
_RcftSlotLANFxPortCurrentOffsetCurr_Object=MibTableColumn
rcftSlotLANFxPortCurrentOffsetCurr=_RcftSlotLANFxPortCurrentOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,6,1,4),_RcftSlotLANFxPortCurrentOffsetCurr_Type())
rcftSlotLANFxPortCurrentOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentOffsetCurr.setStatus(_A)
class _RcftSlotLANFxPortCurrentRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortCurrentRecvPower_Type.__name__=_C
_RcftSlotLANFxPortCurrentRecvPower_Object=MibTableColumn
rcftSlotLANFxPortCurrentRecvPower=_RcftSlotLANFxPortCurrentRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,6,1,5),_RcftSlotLANFxPortCurrentRecvPower_Type())
rcftSlotLANFxPortCurrentRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentRecvPower.setStatus(_A)
class _RcftSlotLANFxPortCurrentSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortCurrentSendPower_Type.__name__=_C
_RcftSlotLANFxPortCurrentSendPower_Object=MibTableColumn
rcftSlotLANFxPortCurrentSendPower=_RcftSlotLANFxPortCurrentSendPower_Object((1,3,6,1,4,1,8886,2,1,5,6,1,6),_RcftSlotLANFxPortCurrentSendPower_Type())
rcftSlotLANFxPortCurrentSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortCurrentSendPower.setStatus(_A)
_RcftSlotLANFxPortIntervalTable_Object=MibTable
rcftSlotLANFxPortIntervalTable=_RcftSlotLANFxPortIntervalTable_Object((1,3,6,1,4,1,8886,2,1,5,7))
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalTable.setStatus(_A)
_RcftSlotLANFxPortIntervalEntry_Object=MibTableRow
rcftSlotLANFxPortIntervalEntry=_RcftSlotLANFxPortIntervalEntry_Object((1,3,6,1,4,1,8886,2,1,5,7,1))
rcftSlotLANFxPortIntervalEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_I),(0,_E,_K))
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalEntry.setStatus(_A)
_RcftSlotLANFxIntervalNumber_Type=Integer32
_RcftSlotLANFxIntervalNumber_Object=MibTableColumn
rcftSlotLANFxIntervalNumber=_RcftSlotLANFxIntervalNumber_Object((1,3,6,1,4,1,8886,2,1,5,7,1,1),_RcftSlotLANFxIntervalNumber_Type())
rcftSlotLANFxIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxIntervalNumber.setStatus(_A)
class _RcftSlotLANFxPortIntervalTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortIntervalTemperature_Type.__name__=_C
_RcftSlotLANFxPortIntervalTemperature_Object=MibTableColumn
rcftSlotLANFxPortIntervalTemperature=_RcftSlotLANFxPortIntervalTemperature_Object((1,3,6,1,4,1,8886,2,1,5,7,1,2),_RcftSlotLANFxPortIntervalTemperature_Type())
rcftSlotLANFxPortIntervalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalTemperature.setStatus(_A)
class _RcftSlotLANFxPortIntervalVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortIntervalVoltage_Type.__name__=_C
_RcftSlotLANFxPortIntervalVoltage_Object=MibTableColumn
rcftSlotLANFxPortIntervalVoltage=_RcftSlotLANFxPortIntervalVoltage_Object((1,3,6,1,4,1,8886,2,1,5,7,1,3),_RcftSlotLANFxPortIntervalVoltage_Type())
rcftSlotLANFxPortIntervalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalVoltage.setStatus(_A)
class _RcftSlotLANFxPortIntervalOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortIntervalOffsetCurr_Type.__name__=_C
_RcftSlotLANFxPortIntervalOffsetCurr_Object=MibTableColumn
rcftSlotLANFxPortIntervalOffsetCurr=_RcftSlotLANFxPortIntervalOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,7,1,4),_RcftSlotLANFxPortIntervalOffsetCurr_Type())
rcftSlotLANFxPortIntervalOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalOffsetCurr.setStatus(_A)
class _RcftSlotLANFxPortIntervalRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortIntervalRecvPower_Type.__name__=_C
_RcftSlotLANFxPortIntervalRecvPower_Object=MibTableColumn
rcftSlotLANFxPortIntervalRecvPower=_RcftSlotLANFxPortIntervalRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,7,1,5),_RcftSlotLANFxPortIntervalRecvPower_Type())
rcftSlotLANFxPortIntervalRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalRecvPower.setStatus(_A)
class _RcftSlotLANFxPortIntervalSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortIntervalSendPower_Type.__name__=_C
_RcftSlotLANFxPortIntervalSendPower_Object=MibTableColumn
rcftSlotLANFxPortIntervalSendPower=_RcftSlotLANFxPortIntervalSendPower_Object((1,3,6,1,4,1,8886,2,1,5,7,1,6),_RcftSlotLANFxPortIntervalSendPower_Type())
rcftSlotLANFxPortIntervalSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortIntervalSendPower.setStatus(_A)
_RcftSlotWANFxPortTable_Object=MibTable
rcftSlotWANFxPortTable=_RcftSlotWANFxPortTable_Object((1,3,6,1,4,1,8886,2,1,5,8))
if mibBuilder.loadTexts:rcftSlotWANFxPortTable.setStatus(_A)
_RcftSlotWANFxPortEntry_Object=MibTableRow
rcftSlotWANFxPortEntry=_RcftSlotWANFxPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,8,1))
rcftSlotWANFxPortEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_H))
if mibBuilder.loadTexts:rcftSlotWANFxPortEntry.setStatus(_A)
class _RcftSlotWANFxPortTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortTemperature_Type.__name__=_C
_RcftSlotWANFxPortTemperature_Object=MibTableColumn
rcftSlotWANFxPortTemperature=_RcftSlotWANFxPortTemperature_Object((1,3,6,1,4,1,8886,2,1,5,8,1,1),_RcftSlotWANFxPortTemperature_Type())
rcftSlotWANFxPortTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortTemperature.setStatus(_A)
class _RcftSlotWANFxPortVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortVoltage_Type.__name__=_C
_RcftSlotWANFxPortVoltage_Object=MibTableColumn
rcftSlotWANFxPortVoltage=_RcftSlotWANFxPortVoltage_Object((1,3,6,1,4,1,8886,2,1,5,8,1,2),_RcftSlotWANFxPortVoltage_Type())
rcftSlotWANFxPortVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortVoltage.setStatus(_A)
class _RcftSlotWANFxPortOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortOffsetCurr_Type.__name__=_C
_RcftSlotWANFxPortOffsetCurr_Object=MibTableColumn
rcftSlotWANFxPortOffsetCurr=_RcftSlotWANFxPortOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,8,1,3),_RcftSlotWANFxPortOffsetCurr_Type())
rcftSlotWANFxPortOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortOffsetCurr.setStatus(_A)
class _RcftSlotWANFxPortRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortRecvPower_Type.__name__=_C
_RcftSlotWANFxPortRecvPower_Object=MibTableColumn
rcftSlotWANFxPortRecvPower=_RcftSlotWANFxPortRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,8,1,4),_RcftSlotWANFxPortRecvPower_Type())
rcftSlotWANFxPortRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortRecvPower.setStatus(_A)
class _RcftSlotWANFxPortSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotWANFxPortSendPower_Type.__name__=_C
_RcftSlotWANFxPortSendPower_Object=MibTableColumn
rcftSlotWANFxPortSendPower=_RcftSlotWANFxPortSendPower_Object((1,3,6,1,4,1,8886,2,1,5,8,1,5),_RcftSlotWANFxPortSendPower_Type())
rcftSlotWANFxPortSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotWANFxPortSendPower.setStatus(_A)
_RcftSlotLANFxPortTable_Object=MibTable
rcftSlotLANFxPortTable=_RcftSlotLANFxPortTable_Object((1,3,6,1,4,1,8886,2,1,5,9))
if mibBuilder.loadTexts:rcftSlotLANFxPortTable.setStatus(_A)
_RcftSlotLANFxPortEntry_Object=MibTableRow
rcftSlotLANFxPortEntry=_RcftSlotLANFxPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,9,1))
rcftSlotLANFxPortEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_E,_I))
if mibBuilder.loadTexts:rcftSlotLANFxPortEntry.setStatus(_A)
class _RcftSlotLANFxPortTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortTemperature_Type.__name__=_C
_RcftSlotLANFxPortTemperature_Object=MibTableColumn
rcftSlotLANFxPortTemperature=_RcftSlotLANFxPortTemperature_Object((1,3,6,1,4,1,8886,2,1,5,9,1,1),_RcftSlotLANFxPortTemperature_Type())
rcftSlotLANFxPortTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortTemperature.setStatus(_A)
class _RcftSlotLANFxPortVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortVoltage_Type.__name__=_C
_RcftSlotLANFxPortVoltage_Object=MibTableColumn
rcftSlotLANFxPortVoltage=_RcftSlotLANFxPortVoltage_Object((1,3,6,1,4,1,8886,2,1,5,9,1,2),_RcftSlotLANFxPortVoltage_Type())
rcftSlotLANFxPortVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortVoltage.setStatus(_A)
class _RcftSlotLANFxPortOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortOffsetCurr_Type.__name__=_C
_RcftSlotLANFxPortOffsetCurr_Object=MibTableColumn
rcftSlotLANFxPortOffsetCurr=_RcftSlotLANFxPortOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,5,9,1,3),_RcftSlotLANFxPortOffsetCurr_Type())
rcftSlotLANFxPortOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortOffsetCurr.setStatus(_A)
class _RcftSlotLANFxPortRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortRecvPower_Type.__name__=_C
_RcftSlotLANFxPortRecvPower_Object=MibTableColumn
rcftSlotLANFxPortRecvPower=_RcftSlotLANFxPortRecvPower_Object((1,3,6,1,4,1,8886,2,1,5,9,1,4),_RcftSlotLANFxPortRecvPower_Type())
rcftSlotLANFxPortRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortRecvPower.setStatus(_A)
class _RcftSlotLANFxPortSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftSlotLANFxPortSendPower_Type.__name__=_C
_RcftSlotLANFxPortSendPower_Object=MibTableColumn
rcftSlotLANFxPortSendPower=_RcftSlotLANFxPortSendPower_Object((1,3,6,1,4,1,8886,2,1,5,9,1,5),_RcftSlotLANFxPortSendPower_Type())
rcftSlotLANFxPortSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotLANFxPortSendPower.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcftSlotWANFxPortCurrentTable':rcftSlotWANFxPortCurrentTable,'rcftSlotWANFxPortCurrentEntry':rcftSlotWANFxPortCurrentEntry,_H:rcftSlotWANFxPortIndex,'rcftSlotWANFxPortCurrentTemperature':rcftSlotWANFxPortCurrentTemperature,'rcftSlotWANFxPortCurrentVoltage':rcftSlotWANFxPortCurrentVoltage,'rcftSlotWANFxPortCurrentOffsetCurr':rcftSlotWANFxPortCurrentOffsetCurr,'rcftSlotWANFxPortCurrentRecvPower':rcftSlotWANFxPortCurrentRecvPower,'rcftSlotWANFxPortCurrentSendPower':rcftSlotWANFxPortCurrentSendPower,'rcftSlotWANFxPortIntervalTable':rcftSlotWANFxPortIntervalTable,'rcftSlotWANFxPortIntervalEntry':rcftSlotWANFxPortIntervalEntry,_J:rcftSlotWANFxIntervalNumber,'rcftSlotWANFxPortIntervalTemperature':rcftSlotWANFxPortIntervalTemperature,'rcftSlotWANFxPortIntervalVoltage':rcftSlotWANFxPortIntervalVoltage,'rcftSlotWANFxPortIntervalOffsetCurr':rcftSlotWANFxPortIntervalOffsetCurr,'rcftSlotWANFxPortIntervalRecvPower':rcftSlotWANFxPortIntervalRecvPower,'rcftSlotWANFxPortIntervalSendPower':rcftSlotWANFxPortIntervalSendPower,'rcftSlotLANFxPortCurrentTable':rcftSlotLANFxPortCurrentTable,'rcftSlotLANFxPortCurrentEntry':rcftSlotLANFxPortCurrentEntry,_I:rcftSlotLANFxPortIndex,'rcftSlotLANFxPortCurrentTemperature':rcftSlotLANFxPortCurrentTemperature,'rcftSlotLANFxPortCurrentVoltage':rcftSlotLANFxPortCurrentVoltage,'rcftSlotLANFxPortCurrentOffsetCurr':rcftSlotLANFxPortCurrentOffsetCurr,'rcftSlotLANFxPortCurrentRecvPower':rcftSlotLANFxPortCurrentRecvPower,'rcftSlotLANFxPortCurrentSendPower':rcftSlotLANFxPortCurrentSendPower,'rcftSlotLANFxPortIntervalTable':rcftSlotLANFxPortIntervalTable,'rcftSlotLANFxPortIntervalEntry':rcftSlotLANFxPortIntervalEntry,_K:rcftSlotLANFxIntervalNumber,'rcftSlotLANFxPortIntervalTemperature':rcftSlotLANFxPortIntervalTemperature,'rcftSlotLANFxPortIntervalVoltage':rcftSlotLANFxPortIntervalVoltage,'rcftSlotLANFxPortIntervalOffsetCurr':rcftSlotLANFxPortIntervalOffsetCurr,'rcftSlotLANFxPortIntervalRecvPower':rcftSlotLANFxPortIntervalRecvPower,'rcftSlotLANFxPortIntervalSendPower':rcftSlotLANFxPortIntervalSendPower,'rcftSlotWANFxPortTable':rcftSlotWANFxPortTable,'rcftSlotWANFxPortEntry':rcftSlotWANFxPortEntry,'rcftSlotWANFxPortTemperature':rcftSlotWANFxPortTemperature,'rcftSlotWANFxPortVoltage':rcftSlotWANFxPortVoltage,'rcftSlotWANFxPortOffsetCurr':rcftSlotWANFxPortOffsetCurr,'rcftSlotWANFxPortRecvPower':rcftSlotWANFxPortRecvPower,'rcftSlotWANFxPortSendPower':rcftSlotWANFxPortSendPower,'rcftSlotLANFxPortTable':rcftSlotLANFxPortTable,'rcftSlotLANFxPortEntry':rcftSlotLANFxPortEntry,'rcftSlotLANFxPortTemperature':rcftSlotLANFxPortTemperature,'rcftSlotLANFxPortVoltage':rcftSlotLANFxPortVoltage,'rcftSlotLANFxPortOffsetCurr':rcftSlotLANFxPortOffsetCurr,'rcftSlotLANFxPortRecvPower':rcftSlotLANFxPortRecvPower,'rcftSlotLANFxPortSendPower':rcftSlotLANFxPortSendPower})