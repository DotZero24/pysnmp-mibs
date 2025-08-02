_E='read-write'
_D='dcmIndex'
_C='SL-DCM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
CleiCode,=mibBuilder.importSymbols('SL-ENTITY-MIB','CleiCode')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
slDcm=ModuleIdentity((1,3,6,1,4,1,4515,1,14))
_DcmTable_Object=MibTable
dcmTable=_DcmTable_Object((1,3,6,1,4,1,4515,1,14,1))
if mibBuilder.loadTexts:dcmTable.setStatus(_A)
_DcmEntry_Object=MibTableRow
dcmEntry=_DcmEntry_Object((1,3,6,1,4,1,4515,1,14,1,1))
dcmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dcmEntry.setStatus(_A)
_DcmIndex_Type=InterfaceIndex
_DcmIndex_Object=MibTableColumn
dcmIndex=_DcmIndex_Object((1,3,6,1,4,1,4515,1,14,1,1,1),_DcmIndex_Type())
dcmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmIndex.setStatus(_A)
_DcmRange_Type=Integer32
_DcmRange_Object=MibTableColumn
dcmRange=_DcmRange_Object((1,3,6,1,4,1,4515,1,14,1,1,2),_DcmRange_Type())
dcmRange.setMaxAccess(_E)
if mibBuilder.loadTexts:dcmRange.setStatus(_A)
_DcmSpacing_Type=Integer32
_DcmSpacing_Object=MibTableColumn
dcmSpacing=_DcmSpacing_Object((1,3,6,1,4,1,4515,1,14,1,1,3),_DcmSpacing_Type())
dcmSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmSpacing.setStatus(_A)
_DcmTemperature_Type=Integer32
_DcmTemperature_Object=MibTableColumn
dcmTemperature=_DcmTemperature_Object((1,3,6,1,4,1,4515,1,14,1,1,4),_DcmTemperature_Type())
dcmTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmTemperature.setStatus(_A)
_DcmIsActive_Type=TruthValue
_DcmIsActive_Object=MibTableColumn
dcmIsActive=_DcmIsActive_Object((1,3,6,1,4,1,4515,1,14,1,1,5),_DcmIsActive_Type())
dcmIsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmIsActive.setStatus(_A)
_DcmFiberCoefficient_Type=Integer32
_DcmFiberCoefficient_Object=MibTableColumn
dcmFiberCoefficient=_DcmFiberCoefficient_Object((1,3,6,1,4,1,4515,1,14,1,1,6),_DcmFiberCoefficient_Type())
dcmFiberCoefficient.setMaxAccess(_E)
if mibBuilder.loadTexts:dcmFiberCoefficient.setStatus(_A)
_DcmMinDispersion_Type=Integer32
_DcmMinDispersion_Object=MibTableColumn
dcmMinDispersion=_DcmMinDispersion_Object((1,3,6,1,4,1,4515,1,14,1,1,7),_DcmMinDispersion_Type())
dcmMinDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmMinDispersion.setStatus(_A)
_DcmMaxDispersion_Type=Integer32
_DcmMaxDispersion_Object=MibTableColumn
dcmMaxDispersion=_DcmMaxDispersion_Object((1,3,6,1,4,1,4515,1,14,1,1,8),_DcmMaxDispersion_Type())
dcmMaxDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcmMaxDispersion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'slDcm':slDcm,'dcmTable':dcmTable,'dcmEntry':dcmEntry,_D:dcmIndex,'dcmRange':dcmRange,'dcmSpacing':dcmSpacing,'dcmTemperature':dcmTemperature,'dcmIsActive':dcmIsActive,'dcmFiberCoefficient':dcmFiberCoefficient,'dcmMinDispersion':dcmMinDispersion,'dcmMaxDispersion':dcmMaxDispersion})