_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
unitTypeMib=ModuleIdentity((1,3,6,1,4,1,3373,1103,506))
if mibBuilder.loadTexts:unitTypeMib.setRevisions(('2017-06-05 00:00','2017-05-23 00:00','2016-10-14 00:00','2016-07-19 00:00','2016-04-05 00:00','2015-03-04 00:00','2014-12-01 00:00','2014-03-19 00:00','2014-02-07 00:00','2013-04-16 00:00'))
_UnitType_ObjectIdentity=ObjectIdentity
unitType=_UnitType_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3))
_UnitTypeUnequipped_ObjectIdentity=ObjectIdentity
unitTypeUnequipped=_UnitTypeUnequipped_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,1))
if mibBuilder.loadTexts:unitTypeUnequipped.setStatus(_A)
_UnitTypeODU_ObjectIdentity=ObjectIdentity
unitTypeODU=_UnitTypeODU_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,5))
if mibBuilder.loadTexts:unitTypeODU.setStatus(_A)
_UnitTypeALFO80HD_ObjectIdentity=ObjectIdentity
unitTypeALFO80HD=_UnitTypeALFO80HD_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,200))
if mibBuilder.loadTexts:unitTypeALFO80HD.setStatus(_A)
_UnitTypeALFO80HDelectrical_ObjectIdentity=ObjectIdentity
unitTypeALFO80HDelectrical=_UnitTypeALFO80HDelectrical_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,201))
if mibBuilder.loadTexts:unitTypeALFO80HDelectrical.setStatus(_A)
_UnitTypeALFO80HDelectricalOptical_ObjectIdentity=ObjectIdentity
unitTypeALFO80HDelectricalOptical=_UnitTypeALFO80HDelectricalOptical_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,202))
if mibBuilder.loadTexts:unitTypeALFO80HDelectricalOptical.setStatus(_A)
_UnitTypeALFO80HDoptical_ObjectIdentity=ObjectIdentity
unitTypeALFO80HDoptical=_UnitTypeALFO80HDoptical_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,203))
if mibBuilder.loadTexts:unitTypeALFO80HDoptical.setStatus(_A)
_UnitTypeAGS20ARI1_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1=_UnitTypeAGS20ARI1_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,210))
if mibBuilder.loadTexts:unitTypeAGS20ARI1.setStatus(_A)
_UnitTypeAGS20ARI2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2=_UnitTypeAGS20ARI2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,211))
if mibBuilder.loadTexts:unitTypeAGS20ARI2.setStatus(_A)
_UnitTypeAGS20ARI4_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4=_UnitTypeAGS20ARI4_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,212))
if mibBuilder.loadTexts:unitTypeAGS20ARI4.setStatus(_A)
_UnitTypeAGS20DRI4_ObjectIdentity=ObjectIdentity
unitTypeAGS20DRI4=_UnitTypeAGS20DRI4_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,213))
if mibBuilder.loadTexts:unitTypeAGS20DRI4.setStatus(_A)
_UnitTypeAGS20ARI1TDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1TDM2=_UnitTypeAGS20ARI1TDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,214))
if mibBuilder.loadTexts:unitTypeAGS20ARI1TDM2.setStatus(_A)
_UnitTypeAGS20ARI1TDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1TDM3=_UnitTypeAGS20ARI1TDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,215))
if mibBuilder.loadTexts:unitTypeAGS20ARI1TDM3.setStatus(_A)
_UnitTypeAGS20ARI2TDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2TDM2=_UnitTypeAGS20ARI2TDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,216))
if mibBuilder.loadTexts:unitTypeAGS20ARI2TDM2.setStatus(_A)
_UnitTypeAGS20ARI2TDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2TDM3=_UnitTypeAGS20ARI2TDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,217))
if mibBuilder.loadTexts:unitTypeAGS20ARI2TDM3.setStatus(_A)
_UnitTypeAGS20ARI4TDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4TDM2=_UnitTypeAGS20ARI4TDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,218))
if mibBuilder.loadTexts:unitTypeAGS20ARI4TDM2.setStatus(_A)
_UnitTypeAGS20ARI4TDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4TDM3=_UnitTypeAGS20ARI4TDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,219))
if mibBuilder.loadTexts:unitTypeAGS20ARI4TDM3.setStatus(_A)
_UnitTypeAGS20DRI4TDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20DRI4TDM2=_UnitTypeAGS20DRI4TDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,220))
if mibBuilder.loadTexts:unitTypeAGS20DRI4TDM2.setStatus(_A)
_UnitTypeAGS20DRI4TDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20DRI4TDM3=_UnitTypeAGS20DRI4TDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,221))
if mibBuilder.loadTexts:unitTypeAGS20DRI4TDM3.setStatus(_A)
_UnitTypeAGS20CORE_ObjectIdentity=ObjectIdentity
unitTypeAGS20CORE=_UnitTypeAGS20CORE_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,222))
if mibBuilder.loadTexts:unitTypeAGS20CORE.setStatus(_A)
_UnitTypeAGS20ARI1DP_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1DP=_UnitTypeAGS20ARI1DP_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,223))
if mibBuilder.loadTexts:unitTypeAGS20ARI1DP.setStatus(_A)
_UnitTypeAGS20ARI1TDM2DP_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1TDM2DP=_UnitTypeAGS20ARI1TDM2DP_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,224))
if mibBuilder.loadTexts:unitTypeAGS20ARI1TDM2DP.setStatus(_A)
_UnitTypeAGS20ARI1TDM3DP_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1TDM3DP=_UnitTypeAGS20ARI1TDM3DP_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,225))
if mibBuilder.loadTexts:unitTypeAGS20ARI1TDM3DP.setStatus(_A)
_UnitTypeALFOplus1_ObjectIdentity=ObjectIdentity
unitTypeALFOplus1=_UnitTypeALFOplus1_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,229))
if mibBuilder.loadTexts:unitTypeALFOplus1.setStatus(_A)
_UnitTypeALFOplus2_ObjectIdentity=ObjectIdentity
unitTypeALFOplus2=_UnitTypeALFOplus2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,230))
if mibBuilder.loadTexts:unitTypeALFOplus2.setStatus(_A)
_UnitTypeAGS20ODU_ObjectIdentity=ObjectIdentity
unitTypeAGS20ODU=_UnitTypeAGS20ODU_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,231))
if mibBuilder.loadTexts:unitTypeAGS20ODU.setStatus(_A)
_UnitTypeALFOplus2XG_ObjectIdentity=ObjectIdentity
unitTypeALFOplus2XG=_UnitTypeALFOplus2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,232))
if mibBuilder.loadTexts:unitTypeALFOplus2XG.setStatus(_A)
_UnitTypeAGS20ARI1TDM2LC_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI1TDM2LC=_UnitTypeAGS20ARI1TDM2LC_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,240))
if mibBuilder.loadTexts:unitTypeAGS20ARI1TDM2LC.setStatus(_A)
_UnitTypeAGS20COREXG_ObjectIdentity=ObjectIdentity
unitTypeAGS20COREXG=_UnitTypeAGS20COREXG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,249))
if mibBuilder.loadTexts:unitTypeAGS20COREXG.setStatus(_A)
_UnitTypeAGS20ARI2XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2XG=_UnitTypeAGS20ARI2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,250))
if mibBuilder.loadTexts:unitTypeAGS20ARI2XG.setStatus(_A)
_UnitTypeAGS20ARI2TDM2XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2TDM2XG=_UnitTypeAGS20ARI2TDM2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,251))
if mibBuilder.loadTexts:unitTypeAGS20ARI2TDM2XG.setStatus(_A)
_UnitTypeAGS20ARI2TDM3XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2TDM3XG=_UnitTypeAGS20ARI2TDM3XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,252))
if mibBuilder.loadTexts:unitTypeAGS20ARI2TDM3XG.setStatus(_A)
_UnitTypeAGS20ARI4XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4XG=_UnitTypeAGS20ARI4XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,253))
if mibBuilder.loadTexts:unitTypeAGS20ARI4XG.setStatus(_A)
_UnitTypeAGS20ARI4TDM2XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4TDM2XG=_UnitTypeAGS20ARI4TDM2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,254))
if mibBuilder.loadTexts:unitTypeAGS20ARI4TDM2XG.setStatus(_A)
_UnitTypeAGS20ARI4TDM3XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4TDM3XG=_UnitTypeAGS20ARI4TDM3XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,255))
if mibBuilder.loadTexts:unitTypeAGS20ARI4TDM3XG.setStatus(_A)
_UnitTypeAGS20ARI2E_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2E=_UnitTypeAGS20ARI2E_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,260))
if mibBuilder.loadTexts:unitTypeAGS20ARI2E.setStatus(_A)
_UnitTypeAGS20ARI2ETDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2ETDM2=_UnitTypeAGS20ARI2ETDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,261))
if mibBuilder.loadTexts:unitTypeAGS20ARI2ETDM2.setStatus(_A)
_UnitTypeAGS20ARI2ETDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2ETDM3=_UnitTypeAGS20ARI2ETDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,262))
if mibBuilder.loadTexts:unitTypeAGS20ARI2ETDM3.setStatus(_A)
_UnitTypeAGS20ARI2EXG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2EXG=_UnitTypeAGS20ARI2EXG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,263))
if mibBuilder.loadTexts:unitTypeAGS20ARI2EXG.setStatus(_A)
_UnitTypeAGS20ARI2ETDM2XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2ETDM2XG=_UnitTypeAGS20ARI2ETDM2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,264))
if mibBuilder.loadTexts:unitTypeAGS20ARI2ETDM2XG.setStatus(_A)
_UnitTypeAGS20ARI2ETDM3XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI2ETDM3XG=_UnitTypeAGS20ARI2ETDM3XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,265))
if mibBuilder.loadTexts:unitTypeAGS20ARI2ETDM3XG.setStatus(_A)
_UnitTypeAGS20ARI4E_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4E=_UnitTypeAGS20ARI4E_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,266))
if mibBuilder.loadTexts:unitTypeAGS20ARI4E.setStatus(_A)
_UnitTypeAGS20ARI4ETDM2_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4ETDM2=_UnitTypeAGS20ARI4ETDM2_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,267))
if mibBuilder.loadTexts:unitTypeAGS20ARI4ETDM2.setStatus(_A)
_UnitTypeAGS20ARI4ETDM3_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4ETDM3=_UnitTypeAGS20ARI4ETDM3_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,268))
if mibBuilder.loadTexts:unitTypeAGS20ARI4ETDM3.setStatus(_A)
_UnitTypeAGS20ARI4EXG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4EXG=_UnitTypeAGS20ARI4EXG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,269))
if mibBuilder.loadTexts:unitTypeAGS20ARI4EXG.setStatus(_A)
_UnitTypeAGS20ARI4ETDM2XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4ETDM2XG=_UnitTypeAGS20ARI4ETDM2XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,270))
if mibBuilder.loadTexts:unitTypeAGS20ARI4ETDM2XG.setStatus(_A)
_UnitTypeAGS20ARI4ETDM3XG_ObjectIdentity=ObjectIdentity
unitTypeAGS20ARI4ETDM3XG=_UnitTypeAGS20ARI4ETDM3XG_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,271))
if mibBuilder.loadTexts:unitTypeAGS20ARI4ETDM3XG.setStatus(_A)
_UnitTypeALFO80HDx_ObjectIdentity=ObjectIdentity
unitTypeALFO80HDx=_UnitTypeALFO80HDx_ObjectIdentity((1,3,6,1,4,1,3373,1103,6,3,280))
if mibBuilder.loadTexts:unitTypeALFO80HDx.setStatus(_A)
mibBuilder.exportSymbols('SIAE-UNITYPE-MIB',**{'unitType':unitType,'unitTypeUnequipped':unitTypeUnequipped,'unitTypeODU':unitTypeODU,'unitTypeALFO80HD':unitTypeALFO80HD,'unitTypeALFO80HDelectrical':unitTypeALFO80HDelectrical,'unitTypeALFO80HDelectricalOptical':unitTypeALFO80HDelectricalOptical,'unitTypeALFO80HDoptical':unitTypeALFO80HDoptical,'unitTypeAGS20ARI1':unitTypeAGS20ARI1,'unitTypeAGS20ARI2':unitTypeAGS20ARI2,'unitTypeAGS20ARI4':unitTypeAGS20ARI4,'unitTypeAGS20DRI4':unitTypeAGS20DRI4,'unitTypeAGS20ARI1TDM2':unitTypeAGS20ARI1TDM2,'unitTypeAGS20ARI1TDM3':unitTypeAGS20ARI1TDM3,'unitTypeAGS20ARI2TDM2':unitTypeAGS20ARI2TDM2,'unitTypeAGS20ARI2TDM3':unitTypeAGS20ARI2TDM3,'unitTypeAGS20ARI4TDM2':unitTypeAGS20ARI4TDM2,'unitTypeAGS20ARI4TDM3':unitTypeAGS20ARI4TDM3,'unitTypeAGS20DRI4TDM2':unitTypeAGS20DRI4TDM2,'unitTypeAGS20DRI4TDM3':unitTypeAGS20DRI4TDM3,'unitTypeAGS20CORE':unitTypeAGS20CORE,'unitTypeAGS20ARI1DP':unitTypeAGS20ARI1DP,'unitTypeAGS20ARI1TDM2DP':unitTypeAGS20ARI1TDM2DP,'unitTypeAGS20ARI1TDM3DP':unitTypeAGS20ARI1TDM3DP,'unitTypeALFOplus1':unitTypeALFOplus1,'unitTypeALFOplus2':unitTypeALFOplus2,'unitTypeAGS20ODU':unitTypeAGS20ODU,'unitTypeALFOplus2XG':unitTypeALFOplus2XG,'unitTypeAGS20ARI1TDM2LC':unitTypeAGS20ARI1TDM2LC,'unitTypeAGS20COREXG':unitTypeAGS20COREXG,'unitTypeAGS20ARI2XG':unitTypeAGS20ARI2XG,'unitTypeAGS20ARI2TDM2XG':unitTypeAGS20ARI2TDM2XG,'unitTypeAGS20ARI2TDM3XG':unitTypeAGS20ARI2TDM3XG,'unitTypeAGS20ARI4XG':unitTypeAGS20ARI4XG,'unitTypeAGS20ARI4TDM2XG':unitTypeAGS20ARI4TDM2XG,'unitTypeAGS20ARI4TDM3XG':unitTypeAGS20ARI4TDM3XG,'unitTypeAGS20ARI2E':unitTypeAGS20ARI2E,'unitTypeAGS20ARI2ETDM2':unitTypeAGS20ARI2ETDM2,'unitTypeAGS20ARI2ETDM3':unitTypeAGS20ARI2ETDM3,'unitTypeAGS20ARI2EXG':unitTypeAGS20ARI2EXG,'unitTypeAGS20ARI2ETDM2XG':unitTypeAGS20ARI2ETDM2XG,'unitTypeAGS20ARI2ETDM3XG':unitTypeAGS20ARI2ETDM3XG,'unitTypeAGS20ARI4E':unitTypeAGS20ARI4E,'unitTypeAGS20ARI4ETDM2':unitTypeAGS20ARI4ETDM2,'unitTypeAGS20ARI4ETDM3':unitTypeAGS20ARI4ETDM3,'unitTypeAGS20ARI4EXG':unitTypeAGS20ARI4EXG,'unitTypeAGS20ARI4ETDM2XG':unitTypeAGS20ARI4ETDM2XG,'unitTypeAGS20ARI4ETDM3XG':unitTypeAGS20ARI4ETDM3XG,'unitTypeALFO80HDx':unitTypeALFO80HDx,'unitTypeMib':unitTypeMib})