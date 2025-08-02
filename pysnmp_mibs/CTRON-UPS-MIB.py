_E='deprecated'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctUPowerSupply,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctUPowerSupply')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtUPS_ObjectIdentity=ObjectIdentity
ctUPS=_CtUPS_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,4,1))
class _CtUpsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,257,258,259,260,261,262,263,264,265,266,267,268)));namedValues=NamedValues(*(('other',1),('aPCModel370',257),('aPCModel400',258),('aPCModel600',259),('aPCModel900',260),('aPCModel1250',261),('aPCModel2000',262),('matrix3000',263),('matrix5000',264),('su700',265),('su1400',266),('su2000XL',267),('aPCGeneric',268)))
_CtUpsID_Type.__name__=_D
_CtUpsID_Object=MibScalar
ctUpsID=_CtUpsID_Object((1,3,6,1,4,1,52,4,1,5,4,1,1),_CtUpsID_Type())
ctUpsID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctUpsID.setStatus(_A)
_CtUpsUpTime_Type=Integer32
_CtUpsUpTime_Object=MibScalar
ctUpsUpTime=_CtUpsUpTime_Object((1,3,6,1,4,1,52,4,1,5,4,1,2),_CtUpsUpTime_Type())
ctUpsUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctUpsUpTime.setStatus(_E)
_CtUpsDisable_Type=Integer32
_CtUpsDisable_Object=MibScalar
ctUpsDisable=_CtUpsDisable_Object((1,3,6,1,4,1,52,4,1,5,4,1,3),_CtUpsDisable_Type())
ctUpsDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctUpsDisable.setStatus(_E)
_CtUpsDisconnect_Type=Integer32
_CtUpsDisconnect_Object=MibScalar
ctUpsDisconnect=_CtUpsDisconnect_Object((1,3,6,1,4,1,52,4,1,5,4,1,4),_CtUpsDisconnect_Type())
ctUpsDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:ctUpsDisconnect.setStatus(_A)
class _CtUpsTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unitOK',1),('unitFailed',2),('badBattery',3),('noRecentTest',4),('underTest',5)))
_CtUpsTest_Type.__name__=_D
_CtUpsTest_Object=MibScalar
ctUpsTest=_CtUpsTest_Object((1,3,6,1,4,1,52,4,1,5,4,1,5),_CtUpsTest_Type())
ctUpsTest.setMaxAccess(_B)
if mibBuilder.loadTexts:ctUpsTest.setStatus(_A)
_CtUpsBatteryCapacity_Type=Integer32
_CtUpsBatteryCapacity_Object=MibScalar
ctUpsBatteryCapacity=_CtUpsBatteryCapacity_Object((1,3,6,1,4,1,52,4,1,5,4,1,6),_CtUpsBatteryCapacity_Type())
ctUpsBatteryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ctUpsBatteryCapacity.setStatus(_A)
_CtUpsACLineVoltsIn_Type=Integer32
_CtUpsACLineVoltsIn_Object=MibScalar
ctUpsACLineVoltsIn=_CtUpsACLineVoltsIn_Object((1,3,6,1,4,1,52,4,1,5,4,1,7),_CtUpsACLineVoltsIn_Type())
ctUpsACLineVoltsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ctUpsACLineVoltsIn.setStatus(_A)
_CtUpsBatteryVoltsOut_Type=Integer32
_CtUpsBatteryVoltsOut_Object=MibScalar
ctUpsBatteryVoltsOut=_CtUpsBatteryVoltsOut_Object((1,3,6,1,4,1,52,4,1,5,4,1,8),_CtUpsBatteryVoltsOut_Type())
ctUpsBatteryVoltsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ctUpsBatteryVoltsOut.setStatus(_A)
mibBuilder.exportSymbols('CTRON-UPS-MIB',**{'ctUPS':ctUPS,'ctUpsID':ctUpsID,'ctUpsUpTime':ctUpsUpTime,'ctUpsDisable':ctUpsDisable,'ctUpsDisconnect':ctUpsDisconnect,'ctUpsTest':ctUpsTest,'ctUpsBatteryCapacity':ctUpsBatteryCapacity,'ctUpsACLineVoltsIn':ctUpsACLineVoltsIn,'ctUpsBatteryVoltsOut':ctUpsBatteryVoltsOut})