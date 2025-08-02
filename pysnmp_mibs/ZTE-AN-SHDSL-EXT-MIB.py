_H='zxAnShdslSpanConfExtEntry'
_G='ZTE-AN-SHDSL-EXT-MIB'
_F='tcpAM32'
_E='tcpAM16'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hdsl2ShdslMIB,hdsl2ShdslSpanConfEntry=mibBuilder.importSymbols('HDSL2-SHDSL-LINE-MIB','hdsl2ShdslMIB','hdsl2ShdslSpanConfEntry')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxAnShdslExtMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1002))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnShdslExtObjects_ObjectIdentity=ObjectIdentity
zxAnShdslExtObjects=_ZxAnShdslExtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1002,1))
_ZxAnShdslSpanConfExtTable_Object=MibTable
zxAnShdslSpanConfExtTable=_ZxAnShdslSpanConfExtTable_Object((1,3,6,1,4,1,3902,1015,1002,1,1))
if mibBuilder.loadTexts:zxAnShdslSpanConfExtTable.setStatus(_A)
_ZxAnShdslSpanConfExtEntry_Object=MibTableRow
zxAnShdslSpanConfExtEntry=_ZxAnShdslSpanConfExtEntry_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1))
if mibBuilder.loadTexts:zxAnShdslSpanConfExtEntry.setStatus(_A)
class _ZxAnShdslSpanConfDataPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('atm',1),('efm',2),('auto',4)))
_ZxAnShdslSpanConfDataPathType_Type.__name__=_B
_ZxAnShdslSpanConfDataPathType_Object=MibTableColumn
zxAnShdslSpanConfDataPathType=_ZxAnShdslSpanConfDataPathType_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1,1),_ZxAnShdslSpanConfDataPathType_Type())
zxAnShdslSpanConfDataPathType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnShdslSpanConfDataPathType.setStatus(_A)
class _ZxAnShdslSpanActualDataPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('efm',2)))
_ZxAnShdslSpanActualDataPathType_Type.__name__=_B
_ZxAnShdslSpanActualDataPathType_Object=MibTableColumn
zxAnShdslSpanActualDataPathType=_ZxAnShdslSpanActualDataPathType_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1,2),_ZxAnShdslSpanActualDataPathType_Type())
zxAnShdslSpanActualDataPathType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnShdslSpanActualDataPathType.setStatus(_A)
class _ZxAnShdslSpanConfPamConstellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_E,1),(_F,2),('auto',4)))
_ZxAnShdslSpanConfPamConstellation_Type.__name__=_B
_ZxAnShdslSpanConfPamConstellation_Object=MibTableColumn
zxAnShdslSpanConfPamConstellation=_ZxAnShdslSpanConfPamConstellation_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1,3),_ZxAnShdslSpanConfPamConstellation_Type())
zxAnShdslSpanConfPamConstellation.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnShdslSpanConfPamConstellation.setStatus(_A)
class _ZxAnShdslSpanActualPamConstellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ZxAnShdslSpanActualPamConstellation_Type.__name__=_B
_ZxAnShdslSpanActualPamConstellation_Object=MibTableColumn
zxAnShdslSpanActualPamConstellation=_ZxAnShdslSpanActualPamConstellation_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1,4),_ZxAnShdslSpanActualPamConstellation_Type())
zxAnShdslSpanActualPamConstellation.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnShdslSpanActualPamConstellation.setStatus(_A)
_ZxAnShdslSpanActualTransmitPower_Type=Integer32
_ZxAnShdslSpanActualTransmitPower_Object=MibTableColumn
zxAnShdslSpanActualTransmitPower=_ZxAnShdslSpanActualTransmitPower_Object((1,3,6,1,4,1,3902,1015,1002,1,1,1,5),_ZxAnShdslSpanActualTransmitPower_Type())
zxAnShdslSpanActualTransmitPower.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnShdslSpanActualTransmitPower.setStatus(_A)
if mibBuilder.loadTexts:zxAnShdslSpanActualTransmitPower.setUnits('0.1 dBm')
_ZxAnShdslExtGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnShdslExtGlobalObjects=_ZxAnShdslExtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1002,2))
class _ZxAnShdslCapabilities_Type(Bits):namedValues=NamedValues(('rfc4319',0))
_ZxAnShdslCapabilities_Type.__name__='Bits'
_ZxAnShdslCapabilities_Object=MibScalar
zxAnShdslCapabilities=_ZxAnShdslCapabilities_Object((1,3,6,1,4,1,3902,1015,1002,2,1),_ZxAnShdslCapabilities_Type())
zxAnShdslCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnShdslCapabilities.setStatus(_A)
hdsl2ShdslSpanConfEntry.registerAugmentions((_G,_H))
zxAnShdslSpanConfExtEntry.setIndexNames(*hdsl2ShdslSpanConfEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{'zte':zte,'zxAn':zxAn,'zxAnShdslExtMib':zxAnShdslExtMib,'zxAnShdslExtObjects':zxAnShdslExtObjects,'zxAnShdslSpanConfExtTable':zxAnShdslSpanConfExtTable,_H:zxAnShdslSpanConfExtEntry,'zxAnShdslSpanConfDataPathType':zxAnShdslSpanConfDataPathType,'zxAnShdslSpanActualDataPathType':zxAnShdslSpanActualDataPathType,'zxAnShdslSpanConfPamConstellation':zxAnShdslSpanConfPamConstellation,'zxAnShdslSpanActualPamConstellation':zxAnShdslSpanActualPamConstellation,'zxAnShdslSpanActualTransmitPower':zxAnShdslSpanActualTransmitPower,'zxAnShdslExtGlobalObjects':zxAnShdslExtGlobalObjects,'zxAnShdslCapabilities':zxAnShdslCapabilities})