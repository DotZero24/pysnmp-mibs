_E='noWarning'
_D='warning'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lenv_ObjectIdentity=ObjectIdentity
lenv=_Lenv_ObjectIdentity((1,3,6,1,4,1,9,2,1))
_EnvPresent_Type=Integer32
_EnvPresent_Object=MibScalar
envPresent=_EnvPresent_Object((1,3,6,1,4,1,9,2,1,77),_EnvPresent_Type())
envPresent.setMaxAccess(_A)
if mibBuilder.loadTexts:envPresent.setStatus(_B)
_EnvTestPt1Descr_Type=DisplayString
_EnvTestPt1Descr_Object=MibScalar
envTestPt1Descr=_EnvTestPt1Descr_Object((1,3,6,1,4,1,9,2,1,78),_EnvTestPt1Descr_Type())
envTestPt1Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt1Descr.setStatus(_B)
_EnvTestPt1Measure_Type=Integer32
_EnvTestPt1Measure_Object=MibScalar
envTestPt1Measure=_EnvTestPt1Measure_Object((1,3,6,1,4,1,9,2,1,79),_EnvTestPt1Measure_Type())
envTestPt1Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt1Measure.setStatus(_B)
_EnvTestPt2Descr_Type=DisplayString
_EnvTestPt2Descr_Object=MibScalar
envTestPt2Descr=_EnvTestPt2Descr_Object((1,3,6,1,4,1,9,2,1,80),_EnvTestPt2Descr_Type())
envTestPt2Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt2Descr.setStatus(_B)
_EnvTestPt2Measure_Type=Integer32
_EnvTestPt2Measure_Object=MibScalar
envTestPt2Measure=_EnvTestPt2Measure_Object((1,3,6,1,4,1,9,2,1,81),_EnvTestPt2Measure_Type())
envTestPt2Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt2Measure.setStatus(_B)
_EnvTestPt3Descr_Type=DisplayString
_EnvTestPt3Descr_Object=MibScalar
envTestPt3Descr=_EnvTestPt3Descr_Object((1,3,6,1,4,1,9,2,1,82),_EnvTestPt3Descr_Type())
envTestPt3Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt3Descr.setStatus(_B)
_EnvTestPt3Measure_Type=Integer32
_EnvTestPt3Measure_Object=MibScalar
envTestPt3Measure=_EnvTestPt3Measure_Object((1,3,6,1,4,1,9,2,1,83),_EnvTestPt3Measure_Type())
envTestPt3Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt3Measure.setStatus(_B)
_EnvTestPt4Descr_Type=DisplayString
_EnvTestPt4Descr_Object=MibScalar
envTestPt4Descr=_EnvTestPt4Descr_Object((1,3,6,1,4,1,9,2,1,84),_EnvTestPt4Descr_Type())
envTestPt4Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt4Descr.setStatus(_B)
_EnvTestPt4Measure_Type=Integer32
_EnvTestPt4Measure_Object=MibScalar
envTestPt4Measure=_EnvTestPt4Measure_Object((1,3,6,1,4,1,9,2,1,85),_EnvTestPt4Measure_Type())
envTestPt4Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt4Measure.setStatus(_B)
_EnvTestPt5Descr_Type=DisplayString
_EnvTestPt5Descr_Object=MibScalar
envTestPt5Descr=_EnvTestPt5Descr_Object((1,3,6,1,4,1,9,2,1,86),_EnvTestPt5Descr_Type())
envTestPt5Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt5Descr.setStatus(_B)
_EnvTestPt5Measure_Type=Integer32
_EnvTestPt5Measure_Object=MibScalar
envTestPt5Measure=_EnvTestPt5Measure_Object((1,3,6,1,4,1,9,2,1,87),_EnvTestPt5Measure_Type())
envTestPt5Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt5Measure.setStatus(_B)
_EnvTestPt6Descr_Type=DisplayString
_EnvTestPt6Descr_Object=MibScalar
envTestPt6Descr=_EnvTestPt6Descr_Object((1,3,6,1,4,1,9,2,1,88),_EnvTestPt6Descr_Type())
envTestPt6Descr.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt6Descr.setStatus(_B)
_EnvTestPt6Measure_Type=Integer32
_EnvTestPt6Measure_Object=MibScalar
envTestPt6Measure=_EnvTestPt6Measure_Object((1,3,6,1,4,1,9,2,1,89),_EnvTestPt6Measure_Type())
envTestPt6Measure.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt6Measure.setStatus(_B)
_EnvTestPt1MarginVal_Type=Integer32
_EnvTestPt1MarginVal_Object=MibScalar
envTestPt1MarginVal=_EnvTestPt1MarginVal_Object((1,3,6,1,4,1,9,2,1,90),_EnvTestPt1MarginVal_Type())
envTestPt1MarginVal.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt1MarginVal.setStatus(_B)
_EnvTestPt2MarginVal_Type=Integer32
_EnvTestPt2MarginVal_Object=MibScalar
envTestPt2MarginVal=_EnvTestPt2MarginVal_Object((1,3,6,1,4,1,9,2,1,91),_EnvTestPt2MarginVal_Type())
envTestPt2MarginVal.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt2MarginVal.setStatus(_B)
_EnvTestPt3MarginPercent_Type=Integer32
_EnvTestPt3MarginPercent_Object=MibScalar
envTestPt3MarginPercent=_EnvTestPt3MarginPercent_Object((1,3,6,1,4,1,9,2,1,92),_EnvTestPt3MarginPercent_Type())
envTestPt3MarginPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt3MarginPercent.setStatus(_B)
_EnvTestPt4MarginPercent_Type=Integer32
_EnvTestPt4MarginPercent_Object=MibScalar
envTestPt4MarginPercent=_EnvTestPt4MarginPercent_Object((1,3,6,1,4,1,9,2,1,93),_EnvTestPt4MarginPercent_Type())
envTestPt4MarginPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt4MarginPercent.setStatus(_B)
_EnvTestPt5MarginPercent_Type=Integer32
_EnvTestPt5MarginPercent_Object=MibScalar
envTestPt5MarginPercent=_EnvTestPt5MarginPercent_Object((1,3,6,1,4,1,9,2,1,94),_EnvTestPt5MarginPercent_Type())
envTestPt5MarginPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt5MarginPercent.setStatus(_B)
_EnvTestPt6MarginPercent_Type=Integer32
_EnvTestPt6MarginPercent_Object=MibScalar
envTestPt6MarginPercent=_EnvTestPt6MarginPercent_Object((1,3,6,1,4,1,9,2,1,95),_EnvTestPt6MarginPercent_Type())
envTestPt6MarginPercent.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt6MarginPercent.setStatus(_B)
_EnvTestPt1last_Type=Integer32
_EnvTestPt1last_Object=MibScalar
envTestPt1last=_EnvTestPt1last_Object((1,3,6,1,4,1,9,2,1,96),_EnvTestPt1last_Type())
envTestPt1last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt1last.setStatus(_B)
_EnvTestPt2last_Type=Integer32
_EnvTestPt2last_Object=MibScalar
envTestPt2last=_EnvTestPt2last_Object((1,3,6,1,4,1,9,2,1,97),_EnvTestPt2last_Type())
envTestPt2last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt2last.setStatus(_B)
_EnvTestPt3last_Type=Integer32
_EnvTestPt3last_Object=MibScalar
envTestPt3last=_EnvTestPt3last_Object((1,3,6,1,4,1,9,2,1,98),_EnvTestPt3last_Type())
envTestPt3last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt3last.setStatus(_B)
_EnvTestPt4last_Type=Integer32
_EnvTestPt4last_Object=MibScalar
envTestPt4last=_EnvTestPt4last_Object((1,3,6,1,4,1,9,2,1,99),_EnvTestPt4last_Type())
envTestPt4last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt4last.setStatus(_B)
_EnvTestPt5last_Type=Integer32
_EnvTestPt5last_Object=MibScalar
envTestPt5last=_EnvTestPt5last_Object((1,3,6,1,4,1,9,2,1,100),_EnvTestPt5last_Type())
envTestPt5last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt5last.setStatus(_B)
_EnvTestPt6last_Type=Integer32
_EnvTestPt6last_Object=MibScalar
envTestPt6last=_EnvTestPt6last_Object((1,3,6,1,4,1,9,2,1,101),_EnvTestPt6last_Type())
envTestPt6last.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt6last.setStatus(_B)
class _EnvTestPt1warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt1warn_Type.__name__=_C
_EnvTestPt1warn_Object=MibScalar
envTestPt1warn=_EnvTestPt1warn_Object((1,3,6,1,4,1,9,2,1,102),_EnvTestPt1warn_Type())
envTestPt1warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt1warn.setStatus(_B)
class _EnvTestPt2warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt2warn_Type.__name__=_C
_EnvTestPt2warn_Object=MibScalar
envTestPt2warn=_EnvTestPt2warn_Object((1,3,6,1,4,1,9,2,1,103),_EnvTestPt2warn_Type())
envTestPt2warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt2warn.setStatus(_B)
class _EnvTestPt3warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt3warn_Type.__name__=_C
_EnvTestPt3warn_Object=MibScalar
envTestPt3warn=_EnvTestPt3warn_Object((1,3,6,1,4,1,9,2,1,104),_EnvTestPt3warn_Type())
envTestPt3warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt3warn.setStatus(_B)
class _EnvTestPt4warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt4warn_Type.__name__=_C
_EnvTestPt4warn_Object=MibScalar
envTestPt4warn=_EnvTestPt4warn_Object((1,3,6,1,4,1,9,2,1,105),_EnvTestPt4warn_Type())
envTestPt4warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt4warn.setStatus(_B)
class _EnvTestPt5warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt5warn_Type.__name__=_C
_EnvTestPt5warn_Object=MibScalar
envTestPt5warn=_EnvTestPt5warn_Object((1,3,6,1,4,1,9,2,1,106),_EnvTestPt5warn_Type())
envTestPt5warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt5warn.setStatus(_B)
class _EnvTestPt6warn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_EnvTestPt6warn_Type.__name__=_C
_EnvTestPt6warn_Object=MibScalar
envTestPt6warn=_EnvTestPt6warn_Object((1,3,6,1,4,1,9,2,1,107),_EnvTestPt6warn_Type())
envTestPt6warn.setMaxAccess(_A)
if mibBuilder.loadTexts:envTestPt6warn.setStatus(_B)
_EnvFirmVersion_Type=DisplayString
_EnvFirmVersion_Object=MibScalar
envFirmVersion=_EnvFirmVersion_Object((1,3,6,1,4,1,9,2,1,108),_EnvFirmVersion_Type())
envFirmVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:envFirmVersion.setStatus(_B)
_EnvTechnicianID_Type=DisplayString
_EnvTechnicianID_Object=MibScalar
envTechnicianID=_EnvTechnicianID_Object((1,3,6,1,4,1,9,2,1,109),_EnvTechnicianID_Type())
envTechnicianID.setMaxAccess(_A)
if mibBuilder.loadTexts:envTechnicianID.setStatus(_B)
_EnvType_Type=DisplayString
_EnvType_Object=MibScalar
envType=_EnvType_Object((1,3,6,1,4,1,9,2,1,110),_EnvType_Type())
envType.setMaxAccess(_A)
if mibBuilder.loadTexts:envType.setStatus(_B)
_EnvBurnDate_Type=DisplayString
_EnvBurnDate_Object=MibScalar
envBurnDate=_EnvBurnDate_Object((1,3,6,1,4,1,9,2,1,111),_EnvBurnDate_Type())
envBurnDate.setMaxAccess(_A)
if mibBuilder.loadTexts:envBurnDate.setStatus(_B)
_EnvSerialNumber_Type=DisplayString
_EnvSerialNumber_Object=MibScalar
envSerialNumber=_EnvSerialNumber_Object((1,3,6,1,4,1,9,2,1,112),_EnvSerialNumber_Type())
envSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:envSerialNumber.setStatus(_B)
mibBuilder.exportSymbols('OLD-CISCO-ENV-MIB',**{'lenv':lenv,'envPresent':envPresent,'envTestPt1Descr':envTestPt1Descr,'envTestPt1Measure':envTestPt1Measure,'envTestPt2Descr':envTestPt2Descr,'envTestPt2Measure':envTestPt2Measure,'envTestPt3Descr':envTestPt3Descr,'envTestPt3Measure':envTestPt3Measure,'envTestPt4Descr':envTestPt4Descr,'envTestPt4Measure':envTestPt4Measure,'envTestPt5Descr':envTestPt5Descr,'envTestPt5Measure':envTestPt5Measure,'envTestPt6Descr':envTestPt6Descr,'envTestPt6Measure':envTestPt6Measure,'envTestPt1MarginVal':envTestPt1MarginVal,'envTestPt2MarginVal':envTestPt2MarginVal,'envTestPt3MarginPercent':envTestPt3MarginPercent,'envTestPt4MarginPercent':envTestPt4MarginPercent,'envTestPt5MarginPercent':envTestPt5MarginPercent,'envTestPt6MarginPercent':envTestPt6MarginPercent,'envTestPt1last':envTestPt1last,'envTestPt2last':envTestPt2last,'envTestPt3last':envTestPt3last,'envTestPt4last':envTestPt4last,'envTestPt5last':envTestPt5last,'envTestPt6last':envTestPt6last,'envTestPt1warn':envTestPt1warn,'envTestPt2warn':envTestPt2warn,'envTestPt3warn':envTestPt3warn,'envTestPt4warn':envTestPt4warn,'envTestPt5warn':envTestPt5warn,'envTestPt6warn':envTestPt6warn,'envFirmVersion':envFirmVersion,'envTechnicianID':envTechnicianID,'envType':envType,'envBurnDate':envBurnDate,'envSerialNumber':envSerialNumber})